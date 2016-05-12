# -*- coding: utf-8 -*-
"""
Home Controller
"""

import os
from bottle import Bottle, view, static_file, TEMPLATE_PATH

from .. import settings

# -- http://blog.bottlepy.org/2012/07/20/template-search-path-workaround.html
#import os
#import functools
#MY_TEMPLATE_PATH = [os.path.abspath(os.path.join(os.path.dirname(__file__), \
#    os.path.join('..','views')))]
#view = functools.partial(bottle.view, template_lookup=MY_TEMPLATE_PATH)
# --

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), \
    os.path.join('..', 'views'))))

home_app = Bottle()

@home_app.route('assets/<filepath:path>', name='assets')
def static(filepath):
    """
    Handling Static
    """
    return static_file(filepath, root=settings.STATIC_PATH)

@home_app.route('/', apply=[view('index.html')])
def index():
    """
    Index
    """
    return {'get_url': home_app.get_url}
