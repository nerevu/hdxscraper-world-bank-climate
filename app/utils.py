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

from slugify import slugify


def fetch(**kwargs):
    """Fetches realtime data and generates records"""
    slug = kwargs['location'].replace(' ', '_')
    base = '%s/%s/%s' % (kwargs['BASE_URL'], slug, kwargs['DIR'])
    url = '%s/%s.%s' % (base, slug, kwargs['FILE_EXT'])
    r = requests.get(url, stream=True)
    print(r)

    return {
        'f': r.raw,
        'ext': 'fixed',
        'encoding': r.encoding,
        'first_row': 3,
        'has_header': True,
        'widths': [0, 7, 16, 24, 32, 40]}


def get_name(group_name):
    return group_name.lower()


def normalize(records, **kwargs):
    return records


def filterer(record, **kwargs):
    return True


def parse(record, **kwargs):
    record['rid'] = '%s%s' % (slugify(kwargs['location']), record['year'])
    record['country'] = kwargs['location']
    return record
