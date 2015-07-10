#!/usr/bin/python

import os
import sys
import wsgi
from cherrypy import wsgiserver

sys.path.append("lib")
from app import settings


print ""
print "*** wsgi.py starting"

virtenv                         = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'], 'virtenv')
virtualenv                      = os.path.join(virtenv, 'bin/activate_this.py')
py_version                      = os.environ['OPENSHIFT_PYTHON_VERSION']
py_cache                        = os.path.join(virtenv, 'lib', py_version, 'site-packages')
os.environ['PYTHON_EGG_CACHE']  = os.path.join(py_cache)
wsgi_ip                         = os.environ["OPENSHIFT_PYTHON_IP"]
wsgi_port                       = os.environ["OPENSHIFT_PYTHON_PORT"]
wsgi_host                       = os.environ["OPENSHIFT_GEAR_DNS"]

def show_evar(name):
    try:
        print name + " = " + os.environ[""+name+""]
    except:
        print name + " : not found"

print "*** openshift environment variables:"
show_evar('OPENSHIFT_PYTHON_VERSION')
show_evar('PYTHON_EGG_CACHE')
show_evar('OPENSHIFT_PYTHON_DIR')
show_evar('OPENSHIFT_HOMEDIR')
show_evar('OPENSHIFT_REPO_DIR')
show_evar('OPENSHIFT_PYTHON_IP')
show_evar('OPENSHIFT_PYTHON_PORT')
show_evar('OPENSHIFT_GEAR_DNS')
show_evar('VIRTUAL_ENV')

try:
    execfile(virtualenv, dict(__file__=virtualenv))
    print "*** succeeded venv activation: " + virtualenv 
except IOError:
    print "*** failed venv activation: " + virtualenv 
    exit()

print "*** application config variables:"
settings.SQA_DBENGINE  = "sqlite:///"+os.path.join(os.environ["OPENSHIFT_DATA_DIR"], 'sqlite.db')
settings.TEMPLATE_PATH = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'app', 'views')
print "PROJECT_PATH  = " + settings.PROJECT_PATH
print "TEMPLATE_PATH = " + settings.TEMPLATE_PATH 
print "STATIC_PATH   = " + settings.STATIC_PATH
print "SQA_DBENGINE  = " + str(settings.SQA_DBENGINE)
print "SQA_ECHO      = " + str(settings.SQA_ECHO)
print "SQA_KEYWORD   = " + str(settings.SQA_KEYWORD)
print "SQA_CREATE    = " + str(settings.SQA_CREATE) 
print "SQA_COMMIT    = " + str(settings.SQA_COMMIT) 
print "SQA_USE_KWARGS= " + str(settings.SQA_USE_KWARGS)
print "BOTTLE TMPLTS = ", 
print os.listdir(settings.TEMPLATE_PATH)
print "*** application import"

# http://bottlepy.org/docs/dev/deployment.html
os.chdir(os.path.dirname(__file__))
from app.routes import Routes as application

# --- an example from openshift 
# from wsgiref.simple_server import make_server
# httpd = make_server('localhost', 8051, application)
# --- Wait for a single request, serve it and quit.
# httpd.handle_request()
# httpd.serve_forever()



print "*** starting cherrypy wsgi server"
server = wsgiserver.CherryPyWSGIServer((wsgi_ip, int(wsgi_port)), application, server_name=wsgi_host)
server.start()

print "*** wsgi.py finished"

