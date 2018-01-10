import psycopg2
import time
import calendar
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import auth

s = AsyncIOScheduler()
s.start()


def connectDB(bot):
    conn = psycopg2.connect(dbname=auth.db_name, user=auth.db_user, password=auth.db_pass, host=auth.db_host, port=auth.db_port)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
         id SERIAL PRIMARY KEY,
         userid BIGINT,
         name TEXT
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders(
         id SERIAL PRIMARY KEY,
         userid BIGINT,
         timet BIGINT,
         reminder TEXT
    );
    """)
    conn.commit()
    cursor.close()
    s.add_job(checkReminder, 'interval', minutes=1, args=[conn, bot])
    return conn


async def checkReminder(conn, bot):
    t = calendar.timegm(time.gmtime())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reminders WHERE timet <= %s", [t]) #Square brackets to make int as an indexable list
    rows = cursor.fetchall()
    for row in rows:
        target = await bot.get_user_info(str(row[1]))
        await bot.send_message(target, "Don't forget : " + row[3])
        cursor.execute("DELETE FROM reminders WHERE id = %s", [row[0]])
    conn.commit()
    cursor.close()


def addReminder(conn, id, delay, text):
    t = calendar.timegm(time.gmtime())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders(userid, timet, reminder) VALUES(%s, %s, %s)", (id, t + delay * 60, text))
    conn.commit()
    cursor.close()
