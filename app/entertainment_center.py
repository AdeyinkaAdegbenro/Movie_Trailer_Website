import sqlite3

db_file = 'app.db'

def display_trailers():
    db = sqlite3.connect(db_file)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # get all movie data from table as per requirement
    sql = "SELECT * from MOVIEDATA"
    movie_data = cursor.execute(sql)
    movie_data = movie_data.fetchall()
    # disconnect from server
    db.commit()
    db.close()

    #open movie trailers in browser
    return movie_data



# display_trailers()


