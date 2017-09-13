import sqlite3

'''import cgi
form = cgi.FieldStorage()
#get movie data from html form
mov_title =  form.getvalue('mov_title')
mov_art = form.getvalue('mov_art')
trailer_url = form.getvalue('trailer_url')'''
db_file = 'trailer_website.db'
#insert into database





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

insert('bie','gie','die')