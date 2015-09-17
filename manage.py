#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import vendor
vendor.add('lib')
import click
from bottle import static_file, Bottle, run, TEMPLATE_PATH
from beaker.middleware import SessionMiddleware
from app import settings
from app.routes import routes


TEMPLATE_PATH.insert(0, settings.TEMPLATE_PATH)
SESSION_OPTS = {
    'session.type': 'file',
    'session.auto': True
}


my_app = SessionMiddleware(Bottle(), SESSION_OPTS)
# Bottle Routes
my_app.wrap_app.merge(routes)


@my_app.wrap_app.route('/assets/<path:path>', name='assets')
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
    run(app=my_app, host=ip, port=port, debug=debug, reloader=debug)


def unittest_body():
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    test_runner = unittest.runner.TextTestRunner()
    test_runner.run(tests)


def webtest_body():

    print
    print "----------------------------------------------------------------------"

    import uuid
    from webtest import TestApp
    test_app = TestApp(my_app)
    nr_tests = 0

    # return json
    resp = test_app.get('/list/api')
    assert resp.status == '200 OK'
    assert resp.status_int == 200
    assert resp.content_type == 'application/json'
    nr_tests += 1

    # save a link into db
    resp = test_app.get('/list')
    assert resp.status == '200 OK'
    assert resp.status_int == 200
    form = resp.forms[0]
    ex_url = "http://" + uuid.uuid1().urn + ".ex"
    ex_name = uuid.uuid1()
    form["url-input"].value = ex_url
    form["comment-input"].value = ex_name
    resp = form.submit("save")
    assert resp.status == '302 Found'
    assert resp.status_int == 302
    nr_tests += 1

    print "Ran " + str(nr_tests) + " tests\n\nOK"


def behavetest_body():
    print
    print "----------------------------------------------------------------------"
    os.system("pew in bottle-cuturl behave")
    print
    print "OK"


@cmds.command()
def unittests():
    unittest_body()


@cmds.command()
def webtests():
    webtest_body()


@cmds.command()
def behavetests():
    behavetest_body()


@cmds.command()
def alltests():
    unittest_body()
    webtest_body()
    behavetest_body()


@cmds.command()
@click.option('--db', default='data/sqlite.db', type=str,
              help=u'Set path for the db to remove!')
def rmsqlitedb(database):
    try:
        os.remove(database)
        click.echo('Removed {0}!'.format(database))
    except OSError:
        click.echo('Not possible to remove, {0} not found!'.format(database))


if __name__ == "__main__":
    cmds()
