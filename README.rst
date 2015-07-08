

=============
Bottle-cuturl
=============

v0.0.6

A simple favourites / URL shortening app in Python.

Based on:

- `Bottle`_ (microframework)

- SQLite (todo: move to PostgreSQL) with `SQLAlchemy`_ (ORM)

- `cookiecutter-bottle`_ template

Deployed to Heroku: http://fathomless-everglades-8154.herokuapp.com/

Quickstart
----------

Running in development mode (prepare virtual environment and run the app inside):

.. code-block:: bash

    devinit.sh
    devrun.sh

.. image:: https://travis-ci.org/BartGo/bottle-cuturl.svg?branch=master
    :target: https://travis-ci.org/BartGo/bottle-cuturl

.. image:: https://requires.io/github/BartGo/bottle-cuturl/requirements.svg?branch=master
     :target: https://requires.io/github/BartGo/bottle-cuturl/requirements/?branch=master
     :alt: Requirements Status
     
.. _cookiecutter-bottle: https://github.com/avelino/cookiecutter-bottle
.. _bottle: http://bottlepy.org/docs/dev/index.html
.. _sqlalchemy: http://www.sqlalchemy.org/
