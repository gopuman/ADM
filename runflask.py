import logging
import click
import sys
sys.path.append('viz')
from app import app

def runFlask():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    def secho(text, file=None, nl=None, err=None, color=None, **styles):
        pass

    def echo(text, file=None, nl=None, err=None, color=None, **styles):
        pass

    click.echo = echo
    click.secho = secho
    print("Check out the images generated from the DnD campaign -- 127.0.0.1:5000!")
    app.run()