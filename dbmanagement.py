import psycopg2
import time
import calendar
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import auth
import random
import tools

s = AsyncIOScheduler()


def connectDB(bot, reddit, sublist):
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reddit(
             id SERIAL PRIMARY KEY,
             postid VARCHAR UNIQUE,
             url VARCHAR,
             subreddit VARCHAR
        );
        """)
    conn.commit()
    cursor.close()
    for sub in sublist:
        s.add_job(fillPostsInDB, args=[conn, reddit, sub])                      #run the job once immediately
        s.add_job(fillPostsInDB, 'interval', hours=1, args=[conn, reddit, sub]) #then run it every hour
    s.add_job(checkReminder, 'interval', minutes=1, args=[conn, bot])
    s.start()
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


async def addReminder(conn, id, delay, text):
    t = calendar.timegm(time.gmtime())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders(userid, timet, reminder) VALUES(%s, %s, %s)", (id, t + delay * 60, text))
    conn.commit()
    cursor.close()


# We build a database containing images from the subreddits that doesn't support the default random function
# See tools > fetch for more details
def fillPostsInDB(conn, reddit, subname):
    cursor = conn.cursor()
    sub = reddit.subreddit(subname)
    insert = 0
    for post in sub.new(limit=1000):
        # for each post, we filter the url, to check if it's a picture
        if tools.check_img_link(post.url):
            cursor.execute("INSERT INTO reddit(postid, url, subreddit) VALUES(%s, %s, %s) ON CONFLICT (postid) DO NOTHING", (post.id, post.url, subname))
            insert += cursor.rowcount
    conn.commit()
    if insert:
        print("database updated for r/" + subname + ". " + str(insert) + " new lines.")
    else:
        print("database for r/" + subname + " is already up-to-date.")
    cursor.close()

# We get a random post from the cache database.
# That way, we still have a good processing speed, and a lot of random pictures available
# We only return the url, as this is the only thing we want
async def getRandomPostFromDB(conn, subname):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reddit WHERE subreddit = %s", [subname])
    rows = cursor.fetchall()
    rd = random.randint(0, cursor.rowcount)
    randompost = rows[rd]
    cursor.close()
    return randompost[2]

async def execQuery(conn, query):
    cursor = conn.cursor()
    print(query)
    type = query.split(" ")[0].lower()
    print(type)
    message = ""
    if type not in ["select", "delete", "insert"]:
        cursor.close()
        message = "Wrong query type"
        return message
    cursor.execute(query)
    if type == "select":
        if cursor.rowcount > 5:
            message = f"Displaying only first 5 results out of {cursor.rowcount} \n"
        else:
            message = str(cursor.rowcount) + " result(s)"
        rows = cursor.fetchall()
        i = 1
        for row in rows:
            message += str(row) + "\n"
            i += 1
            if i > 5:
                break
    if type == "delete":
        message = str(cursor.rowcount) + " lines deleted"
    if type == "insert":
        message = str(cursor.rowcount) + " lines inserted"
    conn.commit()
    cursor.close()
    return message
