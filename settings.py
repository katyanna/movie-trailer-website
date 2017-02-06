import os
import tmdbsimple as tmdb

tmdb.API_KEY = os.environ.get('TMDB_KEY')
