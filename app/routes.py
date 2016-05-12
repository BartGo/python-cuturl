# -*- coding: utf-8 -*-
"""
Bottle Routes
"""

import bottle

from .controllers.home import home_app
from .controllers.list import list_app

#from . import settings

routes = bottle.Bottle()
routes.merge(home_app)
routes.mount("/list", list_app)
