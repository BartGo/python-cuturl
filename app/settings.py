# -*- coding: utf-8 -*-
import os

APP_NAME = 'python-cuturl'

# Paths
PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'assets')

# SQL Alchemy Settings
SQA_ECHO = True
SQA_KEYWORD = 'db'
SQA_CREATE = True
SQA_COMMIT = True
SQA_USE_KWARGS = False
SQA_DBENGINE = os.environ["DATABASE_URL"]
if ("postgresql+psycopg2" in SQA_DBENGINE):
  try:
    import psycopg2
    # For windows, add to PATH: C:\Program Files\PostgreSQL\...\bin
    # Note, DATABASE_URL is an environment variable used by Heroku;
    # Therefore, override in the dev environment if using a local setup
  except (OSError, ImportError, KeyError):
    raise Exception('PostgreSQL can not be used, psycopg2 import failed!')
