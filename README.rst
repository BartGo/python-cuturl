

=============
Python-cuturl
=============

v0.0.22

A simple favourites / URL shortening app in Python. Work in progress. A project to test tools and environments.

http://fathomless-everglades-8154.herokuapp.com/

Quickstart
----------

Running in development mode (prepare virtual environment and run the app inside):

.. code-block:: bash

    devinit.sh
    devrun.sh

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

.. image:: https://travis-ci.org/BartGo/python-cuturl.svg?branch=master
    :target: https://travis-ci.org/BartGo/python-cuturl

.. image:: https://semaphoreci.com/api/v1/projects/82f94cd9-6144-4e99-966e-649ca567a603/531764/badge.svg
    :target: https://semaphoreci.com/bartgo/python-cuturl

.. image:: https://codeship.com/projects/b9cd91a0-0880-0133-b16d-52c6dae51101/status?branch=master
    :target: https://codeship.com/projects/90320
    :alt: Codeship Status

.. image:: https://circleci.com/gh/BartGo/python-cuturl/tree/master.svg?style=svg
    :target: https://circleci.com/gh/BartGo/python-cuturl/tree/master

.. image:: https://requires.io/github/BartGo/python-cuturl/requirements.svg?branch=master
     :target: https://requires.io/github/BartGo/python-cuturl/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://codecov.io/gh/BartGo/python-cuturl/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/BartGo/python-cuturl
  
.. image:: http://img.shields.io/pypi/v/python-cuturl.svg
     :target: https://pypi.python.org/pypi/python-cuturl
     :alt: PyPI

.. _cookiecutter-bottle: https://github.com/avelino/cookiecutter-bottle
.. _bottle: http://bottlepy.org/docs/dev/index.html
.. _sqlalchemy: http://www.sqlalchemy.org/


