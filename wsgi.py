#!/usr/bin/python
import os
import sys
print "*** wsgi.py starting"
virtenv                         = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv                      = os.path.join(virtenv, 'bin/activate_this.py')
py_version                      = os.environ['OPENSHIFT_PYTHON_VERSION']
py_cache                        = os.path.join(virtenv, 'lib', py_version, 'site-packages')
os.environ['PYTHON_EGG_CACHE']  = os.path.join(py_cache)
def show_evar(name):
    try:
        print name + " = " + os.environ[""+name+""]
    except:
        print name + " : not found"
        pass
    return
print "*** openshift environment variables:"
show_evar('OPENSHIFT_PYTHON_VERSION')
show_evar('PYTHON_EGG_CACHE')
show_evar('OPENSHIFT_PYTHON_DIR')
show_evar('OPENSHIFT_HOMEDIR')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
    print "*** succeeded venv activation: " + virtualenv 
except IOError:
    print "*** failed venv activation: " + virtualenv 
    pass
sys.path.append("lib")
from app import settings
print "*** app environment variables:"
def show_pvar(name):
    try:
        print name + " = " + os.environ[""+name+""]
    except:
        print name + " : not found"
        pass
    return
print "*** config variables:"
SQA_DBENGINE=os.environ["OPENSHIFT_DATA_DIR"]
show_pvar('PROJECT_PATH')
show_pvar('TEMPLATE_PATH') 
show_pvar('STATIC_PATH')
show_pvar('SQA_DBENGINE') # 'sqlite:///data//sqlite.db'
show_pvar('SQA_ECHO') 
show_pvar('SQA_KEYWORD') 
show_pvar('SQA_CREATE') 
show_pvar('SQA_COMMIT') 
show_pvar('SQA_USE_KWARGS')
from app.routes import Routes as application
print "*** wsgi.py finished"
