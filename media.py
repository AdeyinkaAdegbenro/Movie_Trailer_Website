
class Movie(object):
    """This class stores movie related information \
    such as movie title, poster image url, and the movie's youtube url"""
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
