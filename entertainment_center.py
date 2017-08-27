from media import Movie
from fresh_tomatoes import open_movies_page

# creating Movie instances

wonder_woman = Movie('Wonder Woman',
                     'https://upload.wikimedia.org/wikipedia/'
                     'en/e/ed/Wonder_Woman_%282017_film%29.jpg',
                     'https://www.youtube.com/watch?v=VSB4wGIdDwo'
                     )

perfect_guy = Movie('The Perfect Guy',
                    'https://upload.wikimedia.org/wikipedia/en/'
                    'thumb/1/12/ThePerfectGuyPoster.jpg'
                    '/220px-ThePerfectGuyPoster.jpg',
                    'https://www.youtube.com/watch?v=CikoxQ4ytI4'
                    )

the_martian = Movie('The Martian',
                    'https://upload.wikimedia.org/wikipedia/en/thumb/'
                    'c/cd/The_Martian_film_poster.jpg/220px'
                    '-The_Martian_film_poster.jpg',
                    'https://www.youtube.com/watch?v=ej3ioOneTy8'
                    )

joy = Movie('Joy',
            'https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/'
            'Joyfilmposter.jpg/220px-Joyfilmposter.jpg',
            'https://www.youtube.com/watch?v=uR-2TiQVY-k'
            )

victor_frankenstein = Movie('Victor Frankenstein',
                            'https://upload.wikimedia.org/wikipedia/'
                            'en/thumb/4/43/Victor_Frankenstein_2015'
                            '.jpg/220px-Victor_Frankenstein_2015.jpg',
                            'https://www.youtube.com/watch?v=7pxZxY_Siyc'
                            )

deadpool = Movie('Deadpool',
                 'https://upload.wikimedia.org/wikipedia/en/'
                 'thumb/4/46/Deadpool_poster.jpg'
                 '/220px-Deadpool_poster.jpg',
                 'https://www.youtube.com/watch?v=9vN6DHB6bJc'
                 )
# pass movie list to open_movie_page function

movies = [wonder_woman, perfect_guy,
          the_martian, joy, victor_frankenstein, deadpool
          ]
open_movies_page(movies)
