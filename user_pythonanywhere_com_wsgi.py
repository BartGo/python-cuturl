# -*- coding: utf-8 -*-
# not working yet

import os
import sys
from bottle import Bottle
# from beaker.middleware import SessionMiddleware

os.environ['TEST_ENV'] = 'True'

path = os.path.join('home','bgolda','bottle-cuturl.git','app')
if path not in sys.path:
    sys.path.append(path)

SESSION_OPTS = {
    'session.type': 'file',
    'session.auto': True
}

main_app = Bottle() # SessionMiddleware(Bottle(), SESSION_OPTS)

import controllers
import controllers.home
import controllers.home.home_app

main_app.merge(controllers.home.home_app)


