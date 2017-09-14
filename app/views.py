from flask import Flask
from flask import render_template, url_for, request, redirect,flash,Markup, session
import entertainment_center , insert_data
import re

app =Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
						SECRET_KEY='development key'))

@app.route('/fresh_tomatoes', methods=['GET', 'POST'])
def fresh_tomatoes():
	if request.method == "GET":
		#get movies from database
		movies = entertainment_center.display_trailers()
		movie_tiles = ''
		movie_tile_content = '''
						<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    					<img src="{poster_image_url}" width="220" height="342">
    					<h2>{movie_title}</h2>
   
						</div>
						'''
		for movie in movies:
    	    # Extract the youtube ID from the url
			youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie[2])
			youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie[2])
			trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

			# Append the tile for the movie with its content filled in
			movie_tiles += movie_tile_content.format(
				movie_title=movie[0],
				poster_image_url=movie[1],
				trailer_youtube_id=trailer_youtube_id
			)
			
		# make the movie markup safe to display as html instead of plain text in browser
		movie_tiles = {"content":Markup(movie_tiles)}
		#returns html page 
		return render_template('fresh_tomatoes.html', movie_tiles=movie_tiles)

	elif request.method == "POST":
		# get form values
		mov_title, mov_art, trailer_url = request.form['mov_title'], request.form['mov_art'], request.form['trailer_url']
		#insert into the database
		insert_data.insert(mov_title, mov_art, trailer_url)
		#notify user that data added was a success
		flash('Movie Trailer added successfully')
		#refresh page
		return redirect(url_for('fresh_tomatoes'))


if __name__ == "__main__" :
	app.run(debug=True)