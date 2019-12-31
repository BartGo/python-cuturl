# -*- coding: utf-8 -*-
import datetime

from flask import Flask, render_template, make_response, request, jsonify
from slugify import slugify
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


from . import settings

app = Flask(__name__,
    instance_relative_config=False,
    template_folder=settings.TEMPLATE_PATH,
    static_folder=settings.STATIC_PATH) 

# SQL Plugin
if settings.SQA_ECHO == True:
    print("settings.SQA_DBENGINE is " + settings.SQA_DBENGINE)
engine = create_engine(settings.SQA_DBENGINE, echo=settings.SQA_ECHO)

from .models import link

sqa_base = declarative_base()
sqa_base.metadata.create_all(engine)
#plugin = sqlalchemy.Plugin(
#    engine,
#    sqa_base.metadata,
#    keyword=settings.SQA_KEYWORD,
#    create=settings.SQA_CREATE,
#    commit=settings.SQA_COMMIT,
#    use_kwargs=settings.SQA_USE_KWARGS
#)
#app.install(plugin) 
  
# Route methods

def index():
    return(render_template("index.html"))

def static(filepath):
    # print(filepath)
    return static_file(filepath, root=settings.STATIC_PATH)

def list():
    links = db.query(Link)
    return {'links': links, 'get_url': list_app.get_url}

def api_list():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    headers = {"Content-Type": "application/json"}
    links = db.query(Link)
    jlinks = { }
    for link in links:
        jlinks[link.slug] = { 'url' : link.url, 'description' : link.description, 'create_time' : str(link.create_time) }
    return make_response({'links': jsonify(jlinks)}, 200, headers=headers)

def link(slug):
    this_link = db.query(Link).filter_by(slug=slug).first()
    if this_link:
        return {'link': this_link, 'get_url': list_app.get_url}
    return HTTPError(404, 'Link not found.')

def add():
    if request.POST.get('url-input','').strip():
       url = request.POST.get('url-input', '').strip()
    else:
       redirect("/list/")
    if request.POST.get('comment-input','').strip():
       description = request.POST.get('comment-input', '').strip()
    else:
       description = ""
    db.add(Link(url=url, description=description, slug=slugify(url), create_time=datetime.datetime.now()))
    redirect("/list/")

app.add_url_rule('/', index)
app.add_url_rule('/assets/<path:filepath>', static)
app.add_url_rule('/api', api_list)
app.add_url_rule('/<string:slug>', link)
app.add_url_rule('/add', add)
app.add_url_rule('/list', list)
