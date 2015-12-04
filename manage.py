#!/usr/bin/env python
from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import os.path as p
import swutils
import config

from subprocess import call

from flask import current_app as app
from functools import partial
from flask.ext.script import Manager
from tabutils.process import merge

from app import create_app, db, utils, __title__, models


manager = Manager(create_app)
manager.add_option('-m', '--mode', default='Development')
manager.main = manager.run

_basedir = p.dirname(__file__)


@manager.command
def check():
    """Check staged changes for lint errors"""
    call(p.join(_basedir, 'bin', 'check-stage'), shell=True)


@manager.command
def lint():
    """Check style with flake8"""
    call('flake8')


@manager.command
def pipme():
    """Install requirements.txt"""
    call('sudo pip install -r requirements.txt', shell=True)


@manager.command
def require():
    """Create requirements.txt"""
    cmd = 'pip freeze -l | grep -vxFf dev-requirements.txt > requirements.txt'
    call(cmd, shell=True)


@manager.command
def test():
    """Run nose and script tests"""
    call('nosetests -xv', shell=True)


@manager.command
def createdb():
    """Creates database if it doesn't already exist"""
    with app.app_context():
        db.create_all()
        print('Database created')


@manager.command
def cleardb():
    """Removes all content from database"""
    with app.app_context():
        db.drop_all()
        print('Database cleared')


@manager.command
def setup():
    """Removes all content from database and creates new tables"""
    with app.app_context():
        cleardb()
        createdb()


@manager.command
def run():
    """Populates all tables in db with most recent data"""
    with app.app_context():
        args = (config.RECIPIENT, app.config.get('LOGFILE'), __title__)
        exception_handler = swutils.ExceptionHandler(*args).handler
        extra = {
            'fetch': utils.fetch,
            'get_name': utils.get_name,
            'normalize': utils.normalize,
            'filterer': utils.filterer,
            'parse': utils.parse}

        kwargs = merge([app.config, extra])
        job = partial(swutils.populate, db.engine, models, **kwargs)
        swutils.run_or_schedule(job, app.config['SW'], exception_handler)


@manager.option(
    '-s', '--stag', help='upload to staging site', action='store_true')
def upload(stag=False):
    """Upload files to HDX"""
    call([p.join(_basedir, 'bin', 'upload'), 'stag' if stag else 'prod'])


@manager.option(
    '-s', '--stag', help='upload to staging site', action='store_true')
def update(stag=False):
    """Update dataset metadata"""
    call([p.join(_basedir, 'bin', 'update'), 'stag' if stag else 'prod'])


if __name__ == '__main__':
    manager.run()
