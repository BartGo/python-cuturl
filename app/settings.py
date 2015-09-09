# -*- coding: utf-8 -*-
import os

APP_NAME = 'bottle-cuturl'

# Paths

PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'views')
STATIC_PATH = os.path.join(PROJECT_PATH, 'assets')

# SQL Alchemy 

# *** PostgreSQL
try:
  import psycopg2
  # # for windows, add to PATH: C:\Program Files\PostgreSQL\9.4\bin
  # DATABASE_URL is an environment variable used by Heroku
  SQL_DBENGINE_LOCAL = "postgresql+psycopg2://cuturl:cuturl@localhost:5432/bottle-cuturl"
  SQA_DBENGINE = os.environ["DATABASE_URL"] or SQL_DBENGINE_LOCAL
except:
  # *** SQLite
  SQA_DBENGINE = 'sqlite:///data//sqlite.db'

SQA_ECHO = True
SQA_KEYWORD = 'db'
SQA_CREATE = True
SQA_COMMIT = True
SQA_USE_KWARGS = False

# Crashreporter

from crashreporter import CrashReporter
cr = CrashReporter(report_dir='crashreporter', check_interval=10, config='.crashreporter.cfg')
cr.application_name = APP_NAME
cr.application_version = '0.0.17' # bumpversion updates that

