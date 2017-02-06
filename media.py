import tmdbsimple as tmdb
import settings

class Movie():
  BASE_IMAGE_PATH = u'https://image.tmdb.org/t/p/w185_and_h278_bestv2/'

  def __init__(self, movie_dict):
    self.raw = movie_dict
    self.id                  = movie_dict['id']
    self.title               = movie_dict['title']
    self.poster_image_path   = movie_dict['poster_path']
    self.release             = movie_dict['release_date']

  def trailer_key(self):
    movie = tmdb.Movies(self.id)
    response = movie.videos()
    trailer_key = response['results'][0]['key']

    if not trailer_key:
      trailer_key = 'rbhrz1-4hN4' # Trailer For Every Oscar-Winning Movie Ever `

    return trailer_key

  def poster_image_url(self):
    return self.BASE_IMAGE_PATH + self.poster_image_path
