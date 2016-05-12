# -*- coding: utf-8 -*-
"""
Bottle Routes
"""

import bottle

from .controllers.home import home_app
from .controllers.list import list_app

#from . import settings

ROUTES = bottle.Bottle()
ROUTES.merge(home_app)
ROUTES.mount("/list", list_app)
