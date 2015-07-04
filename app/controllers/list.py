# -*- coding: utf-8 -*-
from slugify import slugify
from bottle import Bottle, SimpleTemplate as Template, view, redirect, HTTPError, static_file, request
from bottle.ext import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from ..models import engine
from ..models.link import Link

from .. import settings

import datetime

# User application
list_app = Bottle()

# Bottle Plugin
SQLAlchemyBase = declarative_base()
SQLAlchemyBase.metadata.create_all(engine)
plugin = sqlalchemy.Plugin(
    engine,
    SQLAlchemyBase.metadata,
    keyword=settings.SQA_KEYWORD,
    create=settings.SQA_CREATE,
    commit=settings.SQA_COMMIT,
    use_kwargs=settings.SQA_USE_KWARGS
)
list_app.install(plugin) 
   

@list_app.route('/assets/<filepath:path>', name='assets')
def static(filepath):
    print filepath
    return static_file(filepath, root=settings.STATIC_PATH)
        
    
# You can not use two separate decorators route and view due to Bottle issues 
# like https://github.com/bottlepy/bottle/issues/207 - below recommended workaround

@list_app.route('/', apply=[view('list')])
def index(db):
    links = db.query(Link)
    return {'links': links, 'get_url': list_app.get_url}


@list_app.route('/:slug', apply=[view('single')])
def link(db, slug):
    this_link = db.query(Link).filter_by(slug=slug).first()
    if this_link:
        return {'link': this_link, 'get_url': list_app.get_url}
    return HTTPError(404, 'Link not found.')


@list_app.route('/add', method="POST")
def add(db):
    if request.POST.get('url-input','').strip():
       url = request.POST.get('url-input', '').strip()
    else:
       redirect("/list/")
    if request.POST.get('comment-input','').strip():
       description = request.POST.get('url-description', '').strip()
    else:
       description = ""
    db.add(Link(url=url, description=description, slug=slugify(url), create_time=datetime.datetime.now()))
    redirect("/list/")


