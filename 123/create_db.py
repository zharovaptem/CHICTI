import sqlite3

# Создаем подключение к базе данных (или создаем новую, если ее нет)
conn = sqlite3.connect('data/database.db')
cursor = conn.cursor()

# Создаем таблицу Заявки (Requests)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Requests (
        requestID INTEGER PRIMARY KEY,
        startDate TEXT,
        orgTechType TEXT,
        orgTechModel TEXT,
        problemDescription TEXT,
        requestStatus TEXT,
        completionDate TEXT,
        repairParts TEXT,
        masterID INTEGER,
        clientID INTEGER,
        FOREIGN KEY (masterID) REFERENCES Users(userID),
        FOREIGN KEY (clientID) REFERENCES Users(userID)
    )
''')

# Создаем таблицу Пользователи (Users)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        userID INTEGER PRIMARY KEY,
        fio TEXT,
        phone TEXT,
        login TEXT,
        password TEXT,
        type TEXT
    )
''')

# Создаем таблицу Комментарии (Comments)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Comments (
        commentID INTEGER,
        message TEXT,
        masterID INTEGER,
        requestID INTEGER,
        PRIMARY KEY (commentID, masterID, requestID),
        FOREIGN KEY (masterID) REFERENCES Users(userID),
        FOREIGN KEY (requestID) REFERENCES Requests(requestID)
    )
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
