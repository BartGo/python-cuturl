import os
import subprocess
import re

# Remote execution not used yet.
#import fabric

# By convention, venv for the current application is the name
# of the current folder (letters only).
CURR_VENV = re.sub(re.compile('\W'), '', os.getcwd().split(os.sep)[-1])

def ve():
  print "Venv name to be used: " + CURR_VENV

def test():
  subprocess.call("echo Hello from a Fabric script...", shell=True)

def rmve():
  subprocess.call("pew wipeenv " + CURR_VENV, shell=True)
  subprocess.call("pew rm "      + CURR_VENV, shell=True)

def newve():
  #subprocess.call("pew list_pythons", shell=True)
  subprocess.call("pew new -d "  + CURR_VENV, shell=True)

def inve(c):
  subprocess.call("pew in "      + CURR_VENV + " " + c, shell=True)

def lsve():
  inve("pip freeze")   

def reqve():
  inve("pip install -r requirements.txt")

