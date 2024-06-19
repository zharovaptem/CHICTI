import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        userID INTEGER PRIMARY KEY,
        fio TEXT,
        phone TEXT,
        login TEXT,
        password TEXT,
        type TEXT)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Comment(
        commentID INTEGER PRIMARY KEY,
        message TEXT,
        masterID TEXT,
        requestID TEXT)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Requests(
        requestID INTEGER PRIMARY KEY,
        startDate TEXT,
        orgTechType TEXT,
        orgTechModel TEXT,
        problemDescryption TEXT,
        requestStatus TEXT,
        completionDate TEXT,
        repairParts TEXT,
        masterID TEXT,
        clientID TEXT)
""")

con.commit()
con.close()