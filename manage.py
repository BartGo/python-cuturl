#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import vendor
vendor.add('lib')

import click
from bottle import static_file, Bottle, run, TEMPLATE_PATH
from beaker.middleware import SessionMiddleware

from app import settings
from app.routes import routes

TEMPLATE_PATH.insert(0, settings.TEMPLATE_PATH)
session_opts = {
    'session.type': 'file',
    'session.auto': True
}

app = SessionMiddleware(Bottle(), session_opts)

# Bottle Routes
app.wrap_app.merge(routes)


@app.wrap_app.route('/assets/<path:path>', name='assets')
def assets(path):
    yield static_file(path, root=settings.STATIC_PATH)


@click.group()
def cmds():
    pass


@cmds.command()
@click.option('--port', default=os.environ.get('PORT', 8080), type=int,
              help=u'Set application server port!')
@click.option('--ip', default='0.0.0.0', type=str,
              help=u'Set application server ip!')
@click.option('--debug', default=False,
              help=u'Set application server debug!')
def runserver(port, ip, debug):
    click.echo('Start server at: {0}:{1}'.format(ip, port))
    run(app=app, host=ip, port=port, debug=debug, reloader=debug)


@cmds.command()
def test():
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    test_runner = unittest.runner.TextTestRunner()
    test_runner.run(tests)

    
@cmds.command()
@click.option('--db', default='data/sqlite.db', type=str,
              help=u'Set path for the db to remove!')
def rmsqlitedb(db):
    try:
        os.remove(db)
        click.echo('Removed {0}!'.format(db))
    except OSError:
        click.echo('Not possible to remove, {0} not found!'.format(db))
        pass

if __name__ == "__main__":
    cmds()
