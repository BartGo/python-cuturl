# -*- coding: utf-8 -*-
import os

APP_NAME = 'bottle-cuturl'

# Paths

PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'views')
STATIC_PATH = os.path.join(PROJECT_PATH, 'assets')

# SQL Alchemy 

SQA_DBENGINE = 'sqlite:///data//sqlite.db'
SQA_ECHO = True
SQA_KEYWORD = 'db'
SQA_CREATE = True
SQA_COMMIT = True
SQA_USE_KWARGS = False

# Crashreporter

from crashreporter import CrashReporter
cr = CrashReporter(report_dir='~/crashreporter/', check_interval=10, config='./.crashreporter.cfg')
cr.application_name = APP_NAME
cr.application_version = '0.0.11' # bumpversion updates that

