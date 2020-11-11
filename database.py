import sqlite3
import datetime


conn = sqlite3.connect("base.db")
cursor = conn.cursor()

#Записуємо користувача в базу
def addlog(email):
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    cursor.execute("INSERT INTO log(date, time, email) VALUES (\'" + str(date) + "\', \'" + str(time) + "\', \'" + str(email) + "\');")
    conn.commit()