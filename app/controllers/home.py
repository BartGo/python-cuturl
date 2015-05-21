# -*- coding: utf-8 -*-
from bottle import Bottle, view, static_file


home_app = Bottle()


@home_app.route('/assets/<path:path>', name='assets')
def assets(path):
    yield static_file(path, root=settings.STATIC_PATH)
    
    
@home_app.route('/')
@view('index.html')
def index():
  return {'get_url': home_app.get_url}
  