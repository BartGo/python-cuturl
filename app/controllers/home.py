# -*- coding: utf-8 -*-

from bottle import Bottle, view, static_file, TEMPLATE_PATH

from .. import settings

home_app = Bottle()

# -- http://blog.bottlepy.org/2012/07/20/template-search-path-workaround.html
#import os
#import functools
#MY_TEMPLATE_PATH = [
#   os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.join('..','views'))),
#]
#tview = functools.partial(bottle.view, template_lookup=MY_TEMPLATE_PATH)
# --

bottle.TEMPLATE_PATH.insert(0, os.path.join('..','views'))

@home_app.route('assets/<filepath:path>', name='assets')
def static(filepath):
    return static_file(filepath, root=settings.STATIC_PATH)
    
@home_app.route('/', apply=[view('index.html')])
def index():
  return {'get_url': home_app.get_url}
  
