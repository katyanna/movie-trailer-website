Movie trailer website
=====================

The final project for the first course of Udacity's Full Stack Development Nanodegree.
https://movie-trailer-website.herokuapp.com/

Running it
----------

To locally run the app, first you'll need:

- A [TMDB API key](https://www.themoviedb.org/documentation/api).

-  To create a virtualenv
```
$ pip install virtualenv
$ virtualenv environment_name
$ source ./environment_name/bin/activate
```

-  To install [Flask](http://flask.pocoo.org/)
```
$ pip install flask
```

Finally, you can run it with:

```
$ export FLASK_APP=app.py
$ export TMDB_KEY=your_api_key
$ flask run
```
