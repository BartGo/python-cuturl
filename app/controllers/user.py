# -*- coding: utf-8 -*-
from bottle import Bottle, SimpleTemplate as template, view, redirect, HTTPError, static_file
from bottle.ext import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker

from ..models import engine
from ..models.users import User

from .. import settings

# User application
user_app = Bottle()

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
user_app.install(plugin) 
   

@user_app.route('/assets/<filepath:path>', name='assets')
def static(filepath):
    print filepath
    return static_file(filepath, root=settings.STATIC_PATH)
        
    
# You can not use two separate decorators route and view due to Bottle issues 
# like https://github.com/bottlepy/bottle/issues/207 - below recommended workaround

@user_app.route('/', apply=[view('user')])
def index(db):
    users = db.query(User)
    return {'users': users, 'get_url': user_app.get_url}


@user_app.route('/:name', apply=[view('user_view')])
def user(db, name):
    this_user = db.query(User).filter_by(name=name).first()
    if this_user:
        return {'user': this_user, 'get_url': user_app.get_url}
    return HTTPError(404, 'User not found.')


@user_app.route('/add')
def add(db):
    fake = Faker()
    db.add(User(fake.user_name(), fullname=fake.name(), password=fake.sha1()))
    redirect("/user/")


