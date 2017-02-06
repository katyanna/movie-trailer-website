Movie trailer website
=====================

The final project for the first course of Udacity's Full Stack Development Nanodegree.

Running it
----------

To locally run the app, first you'll need:

1. A [TMDB API key](https://www.themoviedb.org/documentation/api).

2. To create a virtualenv

    $ sudo pip install virtualenv
    $ virtualenv nome_do_ambiente
    $ source ./nome_do_ambiente/bin/activate

3. To install [Flask](http://flask.pocoo.org/)

    $ pip install flask

Finally, you can run it with:

    $ export FLASK_APP=tmdb.py
    $ export TMDB_KEY=your_api_key
    $ flask run

