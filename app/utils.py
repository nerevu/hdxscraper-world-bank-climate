#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab

"""
utils
~~~~~

Provides miscellaneous utility methods
"""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import requests

from urllib import urlencode, quote_plus
from slugify import slugify


def fetch(**kwargs):
    """Fetches realtime data and generates records"""
    sub_query = kwargs['SUB_QUERY']
    sub_query['CCode'] = kwargs['code']
    sub_query['thisVariable'] = kwargs['metric']
    sub_string = ','.join('"%s":"%s"' % (k, v) for k, v in sub_query.items())
    sub_quote = '{%s}' % quote_plus(sub_string)
    query = urlencode(kwargs['BASE_QUERY'])
    url = '%s?%s&argumentCollection=%s' % (kwargs['BASE_URL'], query, sub_quote)
    r = requests.get(url)
    return {'records': r.json()}


def get_name(group_name):
    return group_name.lower()


def normalize(records, **kwargs):
    for month, value in enumerate(records):
        yield {'value': value, 'month': month + 1}


def filterer(record, **kwargs):
    return True


def parse(record, **kwargs):
    record['rid'] = '%s-%s-%s' % (kwargs['code'], kwargs['metric'], record['month'])
    record['metric'] = kwargs['metric']
    record['description'] = kwargs['description']
    record['code'] = kwargs['code']
    record['country'] = kwargs['country']
    return record
