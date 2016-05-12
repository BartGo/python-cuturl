# -*- coding: utf-8 -*-

import os
import sys

from bottle import Bottle, run
from beaker.middleware import SessionMiddleware

os.environ['BOTTLE_RUN'] = 'False'

SESSION_OPTS = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

path = os.path.join('home','bgolda','bottle-cuturl.git','app')
if path not in sys.path:
    sys.path.append(path)

import app
from app.controllers import home
#from app.controllers import list

application = SessionMiddleware(Bottle(), SESSION_OPTS)
application.wrap_app.merge(app.controllers.home.home_app)

if os.environ['BOTTLE_RUN'] == 'True':
  run(app=application, debug=True)
