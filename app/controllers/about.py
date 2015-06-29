# -*- coding: utf-8 -*-
from bottle import Bottle, view, static_file

from .. import settings

about_app = Bottle()
    
@about_app.route('/assets/<filepath:path>', name='assets')
def static(filepath):
    print filepath
    return static_file(filepath, root=settings.STATIC_PATH)
    
@about_app.route('/', apply=[view('about')])
def about():
    return {'get_url': about_app.get_url}
