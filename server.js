//Подключение модулей для работы с HTTP запросов, парсинга JSON данных и взаимодействия с SQLITE базой данных
const express = require('express');
const bodyParser = require('body-parser');
const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('plans.db', (err) => {
    if (err) {
        console.error(err.message);
    }
    console.log('Connected to the plans database.');
});

db.run(`CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    time TEXT,
    task TEXT,
    UNIQUE(date, time)
)`);


const app = express(); //Создание экземпляра веб-приложения Express, который будет обрабатывать HTTP запросы и управлять маршрутами.
const port = 3000; //Определение порта, на котором будет запущен веб-сервер

app.use(bodyParser.json()); //Подключение body-parser middleware для парсинга тела запросов в формате JSON
app.use(express.static('.')); //Добавление middleware для обслуживания статических файлов, позволяет серверу обслуживать статические файлы, такие как HTML, CSS и JavaScript

// Получение задач на определенную дату
app.get('/tasks', (req, res) => {
    const date = req.query.date;
    db.all('SELECT time, task FROM tasks WHERE date = ?', [date], (err, rows) => {
        if (err) {
            throw err;
        }
        res.json(rows);
    });
});

// Добавление, обновление или удаление задачи
app.post('/task', (req, res) => {
    const { date, time, task } = req.body;

    // Проверяем, пустое ли поле задачи
    if (task.trim() === '') {
        // Поле задачи пустое, удаляем запись из базы данных
        db.run('DELETE FROM tasks WHERE date = ? AND time = ?', [date, time], function(err) {
            if (err) {
                console.error(err.message);
                res.status(500).send("Произошла ошибка при удалении задачи");
                return;
            }
            if (this.changes === 0) {
                res.send("Такой задачи не найдено для удаления.");
            } else {
                res.send("Задача успешно удалена.");
                console.log(`Задача успешно удалена`);
            }
        });
    } else {
        // Поле задачи не пустое, добавляем или обновляем запись в базе данных
        db.run('INSERT OR REPLACE INTO tasks (date, time, task) VALUES (?, ?, ?)', [date, time, task.trim()], (err) => {
            if (err) {
                console.log(err.message);
                res.status(500).send("Ошибка при добавлении или обновлении задачи");
                return;
            }
            res.send("Задача добавлена или обновлена");
            console.log(`Задача добавлена или обновлена`);
        });
    }
});


app.listen(port, '0.0.0.0', () => {
    console.log(`Server listening at http://localhost:${port}`);
});
