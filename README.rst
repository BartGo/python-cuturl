

=============
Bottle-cuturl
=============

v0.0.17

A simple favourites / URL shortening app in Python.

Based on:

- `Bottle`_ (microframework)

- PostgreSQL with `SQLAlchemy`_ (ORM)

- `cookiecutter-bottle`_ template

Works with Travis CI. Successfull builds are deployed to Heroku:
http://fathomless-everglades-8154.herokuapp.com/

Quickstart
----------

Running in development mode (prepare virtual environment and run the app inside):

.. code-block:: bash

    devinit.sh
    devrun.sh

How am I releasing this to PyPi:

.. code-block:: bash

    # no uncommited changes at this point
    devucl.sh
    bumpversion --allow-dirty patch
    git add .
    git commit -m "Bump version: x.x.x → y.y.y"
    git tag vy.y.y
    git push
    git push --tags
    # .pypirc must be prepared, see http://peterdowns.com/posts/first-time-with-pypi.html
    # python setup.py register -r pypitest
    # python setup.py sdist upload -r pypitest
    # python setup.py register -r pypi
    # python setup.py sdist upload -r pypi
    # python setup.py sdist bdist_wheel upload

.. image:: https://travis-ci.org/BartGo/bottle-cuturl.svg?branch=master
    :target: https://travis-ci.org/BartGo/bottle-cuturl

.. image:: https://semaphoreci.com/api/v1/projects/82f94cd9-6144-4e99-966e-649ca567a603/531764/badge.svg
    :target: https://semaphoreci.com/bartgo/bottle-cuturl

.. image:: https://codeship.com/projects/b9cd91a0-0880-0133-b16d-52c6dae51101/status?branch=master
    :target: https://codeship.com/projects/90320
    :alt: Codeship Status

.. image:: https://drone.io/github.com/BartGo/bottle-cuturl/status.png
    :target: https://drone.io/github.com/BartGo/bottle-cuturl/latest
    :alt: Drone.IO Status


.. image:: https://requires.io/github/BartGo/bottle-cuturl/requirements.svg?branch=master
     :target: https://requires.io/github/BartGo/bottle-cuturl/requirements/?branch=master
     :alt: Requirements Status
     
.. image:: http://www.quantifiedcode.com/api/v1/project/74d7fde00d2d444b879a31e065589de7/badge.svg
     :target: http://www.quantifiedcode.com/app/project/74d7fde00d2d444b879a31e065589de7
     :alt: Code Issues

.. image:: http://img.shields.io/pypi/v/Bottle-Cuturl.svg
     :target: https://pypi.python.org/pypi/Bottle-Cuturl
     :alt: PyPI

.. _cookiecutter-bottle: https://github.com/avelino/cookiecutter-bottle
.. _bottle: http://bottlepy.org/docs/dev/index.html
.. _sqlalchemy: http://www.sqlalchemy.org/


.. image:: https://d2weczhvl823v0.cloudfront.net/BartGo/bottle-cuturl/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

