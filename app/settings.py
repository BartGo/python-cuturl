# -*- coding: utf-8 -*-
import os

APP_NAME = 'python-cuturl'

# disabled but also removed crashreporter==1.11 from setup.py, somehow does not like setuptools==21.0.0
CRASH_REPORT = 0

# Paths

PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'views')
STATIC_PATH = os.path.join(PROJECT_PATH, 'assets')

# SQL Alchemy 

# *** PostgreSQL
SQL_SQLITE_ONLY = 1
SQL_PG_USE_LOCAL = 0
SQL_PG_DBENGINE_LOCAL = "postgresql+psycopg2://cuturl:cuturl@localhost:5432/python-cuturl"

if (not SQL_SQLITE_ONLY):
  try:
    import psycopg2
    # # for windows, add to PATH: C:\Program Files\PostgreSQL\9.4\bin
    # DATABASE_URL is an environment variable used by Heroku
    if SQL_PG_USE_LOCAL == 1:
      SQA_DBENGINE = SQL_PG_DBENGINE_LOCAL
    else:
      SQA_DBENGINE = os.environ["DATABASE_URL"]
  except (OSError, ImportError, KeyError):
    # *** SQLite
    SQL_SQLITE_ONLY = 1 

if SQL_SQLITE_ONLY:
  SQA_DBENGINE = 'sqlite:///data//sqlite.db'


SQA_ECHO = True
SQA_KEYWORD = 'db'
SQA_CREATE = True
SQA_COMMIT = True
SQA_USE_KWARGS = False

# Crashreporter
if CRASH_REPORT == 1:
    from crashreporter import CrashReporter
    cr = CrashReporter(report_dir='crashreporter', check_interval=10, config='.crashreporter.cfg')
    cr.application_name = APP_NAME
    cr.application_version = '0.0.23' # bumpversion updates that

