# -*- coding: utf-8 -*-

import os
import sys

import vendor
vendor.add('lib')

from bottle import static_file, Bottle, run, TEMPLATE_PATH
from beaker.middleware import SessionMiddleware

os.environ['BOTTLE_RUN'] = 'False'

APP_DIR = 'app'

SESSION_OPTS = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

#PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
PROJECT_PATH = os.path.join('home','bgolda','bottle-cuturl.git', APP_DIR)
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'views')
if TEMPLATE_PATH not in sys.path:
    sys.path.append(TEMPLATE_PATH)

STATIC_PATH = os.path.join(PROJECT_PATH, 'assets')
if STATIC_PATH not in sys.path:
    sys.path.append(STATIC_PATH)

import app
from app.controllers import home
#from app.controllers import list

from app import settings
from app.routes import routes

application = SessionMiddleware(Bottle(), SESSION_OPTS)
application.wrap_app.merge(app.controllers.home.home_app)

if os.environ['BOTTLE_RUN'] == 'True':
  run(app=application, debug=True)
