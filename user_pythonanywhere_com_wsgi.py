# -*- coding: utf-8 -*-
# not working yet

import os
import sys
from bottle import Bottle
from beaker.middleware import SessionMiddleware

os.environ['TEST_ENV'] = 'True'
path = '/home/bgolda/bottle-cuturl.git'
if path not in sys.path:
    sys.path.append(path)
path = '/home/bgolda/bottle-cuturl.git/app'
if path not in sys.path:
    sys.path.append(path)

SESSION_OPTS = {
    'session.type': 'file',
    'session.auto': True
}

#from app import controllers
#
#my_app = SessionMiddleware(Bottle(), SESSION_OPTS)
#my_app.wrap_app.merge(controllers.list_app)
