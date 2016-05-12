# -*- coding: utf-8 -*-

import os
import sys

from bottle import Bottle
from beaker.middleware import SessionMiddleware

os.environ['TEST_ENV'] = 'True'

SESSION_OPTS = {
    'session.type': 'file',
    'session.auto': True
}

path = os.path.join('home','bgolda','bottle-cuturl.git','app')
if path not in sys.path:
    sys.path.append(path)

from app.controllers import home

main_app = SessionMiddleware(Bottle(), SESSION_OPTS)
main_app.wrap_app.merge(home.home_app)
