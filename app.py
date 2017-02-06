from flask import Flask
from flask import render_template
import tmdbsimple as tmdb
import media

app = Flask(__name__)

@app.route('/')
def index():
  discover = tmdb.Discover()
  response = discover.movie(release_date_gte = '2017-01-01')
  movies   = response['results']

  movies_list = []
  for movie in movies:
    movies_list.append(media.Movie(movie))

  return render_template('fresh_tomatoes.html', movies = movies_list)
