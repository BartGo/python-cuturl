# -*- coding: utf-8 -*-
from bottle import Bottle

from .controllers.home import home_app
from .controllers.list import list_app
#from .controllers.about import about_app


Routes = Bottle()
Routes.merge(home_app) 
Routes.mount("/list", list_app) 
#Routes.mount("/about", about_app)
