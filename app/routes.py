# -*- coding: utf-8 -*-
from bottle import Bottle

from .controllers.home import home_app
from .controllers.list import list_app
#from .controllers.about import about_app

from . import settings

routes = Bottle()
routes.merge(home_app) 
routes.mount("/list", list_app) 
#routes.mount("/about", about_app)
