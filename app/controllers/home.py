# -*- coding: utf-8 -*-
from bottle import Bottle, view, static_file

from .. import settings

home_app = Bottle()
  
@home_app.route('assets/<filepath:path>', name='assets')
def static(filepath):
    return static_file(filepath, root=settings.STATIC_PATH)
    
    
@home_app.route('/', apply=[view('index')])
def index():
  return {'get_url': home_app.get_url}
  