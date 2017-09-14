import sqlite3
# Open database connection
db = sqlite3.connect('app.db')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS MOVIEDATA")

# Create table as per requirement
sql = """CREATE TABLE MOVIEDATA (
         TITLE  TEXT NOT NULL,
         MOVIE_ART  TEXT NOT NULL,
         YOUTUBE_URL TEXT NOT NULL)"""

cursor.execute(sql)
# disconnect from server
db.commit()
db.close()