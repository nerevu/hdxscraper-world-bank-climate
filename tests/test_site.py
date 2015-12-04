# -*- coding: utf-8 -*-
"""
    app.tests.test_site
    ~~~~~~~~~~~~~~~~~~~

    Provides unit tests for the website.
"""
import nose.tools as nt

from . import APIHelper, app, client
from app import db

tables = []


def setup_module():
    global initialized
    global tables
    global client

    """site initialization"""
    keys = [k for k in app.blueprints.keys() if k.endswith('api0')]
    tables = [k.replace('api0', '') for k in keys]
    db.create_all()
    initialized = True
    print('Site Module Setup\n')


class TestAPI(APIHelper):
    """Unit tests for the API"""
    def __init__(self):
        self.cls_initialized = False

    def test_api_get(self):
        for table in tables:
            n = self.get_num_results(table)
            yield nt.assert_equal, table, n >= 0, True


class TestWeb:
    """Unit tests for the website"""
    def __init__(self):
        self.cls_initialized = False

    def test_home(self):
        r = client.get('/')
        nt.assert_equal(r.status_code, 200)
