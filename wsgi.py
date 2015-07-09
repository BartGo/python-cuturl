#!/usr/bin/python
import os
import sys
print "*** wsgi.py starting"
virtenv                         = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv                      = os.path.join(virtenv, 'bin/activate_this.py')
py_version                      = os.environ['OPENSHIFT_PYTHON_VERSION']
py_cache                        = os.path.join(virtenv, 'lib', py_version, 'site-packages')
os.environ['PYTHON_EGG_CACHE']  = os.path.join(py_cache)
def show_var(name):
    print name + " = " + os.environ[""+name+""]
    return
print "*** openshift environment variables:"
show_var('OPENSHIFT_PYTHON_VERSION')
show_var('PYTHON_EGG_CACHE')
show_var('OPENSHIFT_PYTHON_DIR')
show_var('OPENSHIFT_HOMEDIR')
show_var('PATH_INFO')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
    print "*** succeeded venv activation: " + virtualenv 
except IOError:
    print "*** failed venv activation: " + virtualenv 
    pass
sys.path.append("lib")
from app import settings
from app.routes import Routes as application
print "*** app environment variables:"
show_var('PROJECT_PATH')
show_var('TEMPLATE_PATH') 
show_var('STATIC_PATH')
os.environ['SQA_DBENGINE']=os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 'data', 'sqlite.db') 
show_var('SQA_DBENGINE') # 'sqlite:///data//sqlite.db'
show_var('SQA_ECHO') 
show_var('SQA_KEYWORD') 
show_var('SQA_CREATE') 
show_var('SQA_COMMIT') 
show_var('SQA_USE_KWARGS')
print "*** wsgi.py finished"
