import sqlite3


db_file = 'app.db'

def insert(movie_title, art, trailer_url):
    # Open database connection
    db = sqlite3.connect(db_file)
        

    #db = MySQLdb.connect("localhost","trailer","trailer123","MOVIE_TRAILER" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # insert data into table as per requirement
    sql = "INSERT INTO MOVIEDATA (title,movie_art, youtube_url) VALUES (?, ?, ?)" 
    params = (movie_title, art, trailer_url)
    cursor.execute(sql , params)
    # disconnect from server
    db.commit()
    db.close()
    