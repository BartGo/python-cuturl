# -*- coding: utf-8 -*-

import os
import click

from flask import Flask
from app.routes import app

@click.group()
def cmds():
    pass


def unittest_body():
    # TODO: run tests on a perishable db
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    test_runner = unittest.runner.TextTestRunner()
    test_runner.run(tests)


"""
def webtest_body():

    click.echo("\nRunning web tests...")

    import uuid
    from webtest import TestApp
    test_app  = TestApp(app)
    all_tests = 1
    nr_tests  = 0

    # TODO: implement api, test json response
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
    fake = Factory.create()
    ex_url = fake.url() # "http://" + uuid.uuid1().urn + ".ex"
    ex_name = fake.name() # uuid.uuid1()
    form["url-input"].value = ex_url
    form["comment-input"].value = ex_name
    resp = form.submit("save")
    assert resp.status == '302 Found'
    assert resp.status_int == 302
    nr_tests += 1

    summary = "\nRun " + str(nr_tests) + "/" + str(all_tests)
    click.echo(summary)
"""

@cmds.command()
def unittests():
    unittest_body()


#@cmds.command()
#def webtests():
#    webtest_body()


@cmds.command()
def tests():
    #webtest_body()
    unittest_body()


@cmds.command()
@click.option('--port', default=os.environ.get('PORT', 5000), type=int,
              help=u'Set application server port!')
@click.option('--host', default='0.0.0.0', type=str,
              help=u'Set application server host!')
@click.option('--debug', default=False,
              help=u'Set application server debug!')
def runserver(port, host, debug):
    click.echo('Start server at: {0}:{1}'.format(host, port))  
    app.run(host=host, port=port, debug=debug) 

if __name__ == "__main__":
    cmds()
