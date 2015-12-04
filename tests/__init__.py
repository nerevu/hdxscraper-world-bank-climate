# -*- coding: utf-8 -*-
"""
    tests
    ~~~~~

    Provides application unit tests
"""

from flask.json import loads, dumps
from app import create_app

initialized = False
app = None
client = None
jsonx = None
endpoint = None
base = None


def setup_package():
    """database context creation"""
    global initialized
    global app
    global client
    global jsonx
    global endpoint
    global base

    app = create_app(config_mode='Test')
    endpoint = app.config['API_URL_PREFIX']
    base = '%s/' % endpoint if endpoint else ''
    client = app.test_client()
    jsonx = app.test_request_context()
    jsonx.push()
    initialized = True

    print('Test Package Setup\n')


def teardown_package():
    """database context removal"""
    global initialized
    global jsonx

    jsonx.pop()
    initialized = False

    print('Test Package Teardown\n')


class APIHelper:
    def __init__(self):
        global client
        self.client = client
        self.json = 'application/json'

    def get_data(self, table, id=None, query=None):
        # returns status_code 200

        if id:
            url = base + table + '/' + id
        else:
            url = base + table

        if query:
            r = self.client.get(url, content_type=self.json, q=query)
        else:
            r = self.client.get(url, content_type=self.json)

        return r

    def delete_data(self, table, id):
        # returns status_code 204
        url = '%s/%s/%s' % (endpoint, table, id)
        r = self.client.delete(url, content_type=self.json)
        return r

    def post_data(self, data, table):
        # returns status_code 201
        url = base + table
        r = self.client.post(url, data=dumps(data), content_type=self.json)
        return r

    def patch_data(self, data, table, id=None, query=None):
        # returns status_code 200 or 201
        if id:
            url = base + table + '/' + id
        else:
            url = base + table

        if query:
            r = self.client.patch(
                url, data=dumps(data), content_type=self.json, q=query)
        else:
            r = self.client.patch(url, data=dumps(data), content_type=self.json)

        return r

    def get_num_results(self, table):
        r = self.get_data(table)
        loaded = loads(r.data)
        return loaded['num_results']

    def get_type(self, table, id=1):
        r = self.get_data(table, id)
        loaded = loads(r.data)
        return loaded['type']['id']
