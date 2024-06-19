import sqlite3

def auth(login, password):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT userID, fio, phone, type FROM Users WHERE login = ? AND password = ?''', (login, password))
    data = cursor.fetchone()
    conn.close()
    return data


