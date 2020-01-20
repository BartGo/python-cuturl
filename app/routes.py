# -*- coding: utf-8 -*-
import os
import datetime

from slugify import slugify

from contextlib import contextmanager

from flask import Flask, render_template, make_response, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, Integer, Sequence, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

APP_NAME = 'python-cuturl'

# Paths

PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'assets')

# Create the app

app = Flask(__name__,
    template_folder=TEMPLATE_PATH,
    static_folder=STATIC_PATH) 

# SQL Alchemy setup 

app.config.update(
    SQA_ECHO = True,
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"],
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

if ("postgresql+psycopg2" in app.config['SQLALCHEMY_DATABASE_URI']):
    try:
        import psycopg2
        # For windows, add to PATH: C:\Program Files\PostgreSQL\...\bin
        # Note, DATABASE_URL is an environment variable used by Heroku;
        # Therefore, override in the dev environment if using a local setup
    except (OSError, ImportError, KeyError):
        raise Exception('PostgreSQL can not be used, psycopg2 import failed!')
        exit()

if app.config['SQA_ECHO'] == True:
    print("SQLALCHEMY_DATABASE_URI is " + app.config['SQLALCHEMY_DATABASE_URI'])

Base = declarative_base()

class Link(Base):
    __tablename__ = 'link'
    link_id = Column(Integer, Sequence('link_id_seq'), primary_key=True)
    url = Column(String(1000))
    slug = Column(String(1000))
    description = Column(String(1000))
    create_time = Column(DateTime)

    def __init__(self, slug, url, description, create_time):
        self.url = url
        self.slug = slug
        self.description = description
        self.create_time = create_time

    def __repr__(self):
        rpr = "<Link('{0}', '{1}', '{2}', '{3}')>".format(self.url, self.slug, self.description, self.create_time)
        return rpr
        
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=app.config['SQA_ECHO'])

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
  
# Route methods

def index():
    return(render_template("index.html", title = "My site"))


def static(filepath):
    return static_file(filepath, root=settings.STATIC_PATH)

def list():
    json_links = { }
    with session_scope() as session:
        links = session.query(Link)
        for link in links:
            json_links[link.slug] = { 'url' : link.url, 'description' : link.description, 'create_time' : str(link.create_time) }
   
    print(json_links)
    return render_template("list.html", json_links=links)


def link(slug):
    #BUG: not using css!
    with session_scope() as session:
        links = session.query(Link)
        this_link = session.query(Link).filter_by(slug=slug).first()
        return render_template("single.html", link=this_link)


@app.route('/add',methods = ['POST'])
def add():

    url = request.form.get('url-input')
    comment = request.form.get('comment-input')
    
    if (url and comment):
        with session_scope() as session:
            session.add(Link(url=url, 
                description=comment,
                slug=slugify(url),
                create_time=datetime.datetime.now()))
    
    return redirect("/list", code=302)


# Route bindings

app.add_url_rule('/', 'index', index)
app.add_url_rule('/list', 'list', list)
app.add_url_rule('/assets/<path:filepath>', static)
app.add_url_rule('/list/<string:slug>', 'link', link)

