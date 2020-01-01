# -*- coding: utf-8 -*-

import os
import click

from flask import Flask
from app.routes import app

@click.group()
def cmds():
    pass

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
