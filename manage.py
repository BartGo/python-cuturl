# -*- coding: utf-8 -*-

import os
import click

from flask import Flask
from app.routes import app

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
    app.run() 

if __name__ == "__main__":
    cmds()
