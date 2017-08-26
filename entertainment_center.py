from media import Movie
from fresh_tomatoes import open_movies_page

wonder_woman = Movie('Wonder Woman', 'Before she was Wonder Woman, she was Diana, princess of the Amazons, trained warrior. When a pilot crashes and tells of conflict in the outside world, she leaves home to fight a war, discovering her full powers and true destiny.', 'https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg', 'https://www.youtube.com/watch?v=VSB4wGIdDwo')

perfect_guy = Movie('The Perfect Guy', 'After breaking up with her boyfriend, a professional woman gets involved with a man who seems almost too good to be true.', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/12/ThePerfectGuyPoster.jpg/220px-ThePerfectGuyPoster.jpg','https://www.youtube.com/watch?v=CikoxQ4ytI4')

the_martian = Movie('The Martian', 'An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.', 'https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg', 'https://www.youtube.com/watch?v=ej3ioOneTy8')

joy = Movie('Joy', 'Joy is the story of the title character, who rose to become founder and matriarch of a powerful family business dynasty.', 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Joyfilmposter.jpg/220px-Joyfilmposter.jpg', 'https://www.youtube.com/watch?v=uR-2TiQVY-k')

victor_frankenstein = Movie('Victor Frankenstein', 'Told from Igor\'s perspective, we see the troubled young assistant\'s dark origins, his redemptive friendship with the young medical student Viktor Von Frankenstein, and become eyewitnesses to the emergence of how Frankenstein became the man - and the legend - we know today.', 'https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Victor_Frankenstein_2015.jpg/220px-Victor_Frankenstein_2015.jpg', 'https://www.youtube.com/watch?v=7pxZxY_Siyc')

deadpool = Movie('Deadpool', 'A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.', 'https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Deadpool_poster.jpg/220px-Deadpool_poster.jpg', 'https://www.youtube.com/watch?v=9vN6DHB6bJc')



movies = [wonder_woman, perfect_guy, the_martian, joy, victor_frankenstein, deadpool]
open_movies_page(movies)