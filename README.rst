

=============
Bottle-cuturl
=============

v0.0.6

A simple favourites / URL shortening app in Python.

Based on:

- `Bottle`_ (microframework)

- SQLite (todo: move to PostgreSQL) with `SQLAlchemy`_ (ORM)

- `cookiecutter-bottle`_ template

Works with Travis CI. Successfull builds are deployed to Heroku:
http://fathomless-everglades-8154.herokuapp.com/

Codeship integration in progress.

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
     
.. image:: http://www.quantifiedcode.com/api/v1/project/74d7fde00d2d444b879a31e065589de7/badge.svg
     :target: http://www.quantifiedcode.com/app/project/74d7fde00d2d444b879a31e065589de7
     :alt: Code Issues

.. _cookiecutter-bottle: https://github.com/avelino/cookiecutter-bottle
.. _bottle: http://bottlepy.org/docs/dev/index.html
.. _sqlalchemy: http://www.sqlalchemy.org/
