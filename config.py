# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab

"""
config
~~~~~~

Provides app configuration settings
"""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

from os import path as p

BASEDIR = p.dirname(__file__)
PARENTDIR = p.dirname(BASEDIR)
DB_NAME = 'scraperwiki.sqlite'
RECIPIENT = 'reubano@gmail.com'


class Config(object):
    base = 'http://www.geog.ox.ac.uk'
    BASE_URL = '%s/research/climate/projects/undp-cp/UNDP_data' % base
    FILE_EXT = 'ts.obs.precip.ts.ensemblemean.abs.txt'
    DIR = 'Observed/Mean/Timeseries/Absolute'
    locs = [
        'Afghanistan', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
        'Bangladesh', 'Barbados', 'Belize', 'Benin', 'Cambodia', 'Cameroon',
        'Cape Verde', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Cuba',
        'Dominica', 'Dominican Republic', 'Equatorial Guinea', 'Eritrea',
        'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Grenada', 'Guinea', 'Guyana',
        'Indonesia', 'Jamaica', 'Kenya', 'Lebanon', 'Liberia', 'Malawi', 'Mali',
        'Mauritania', 'Mauritius', 'Mexico', 'Morocco', 'Mozambique', 'Nepal',
        'Nicaragua', 'Nigeria', 'Pakistan', 'Sao Tome and Principe', 'Senegal',
        'Sierra Leone', 'South Africa', 'St Kitts and Nevis', 'St Lucia',
        'St Vincent and the Grenadines', 'Suriname', 'Tanzania', 'The Bahamas',
        'Togo', 'Trinidad and Tobago', 'Uganda', 'Vietnam', 'Yemen', 'Zambia']
    TABLES = [{'name': 'climate', 'location': 'Afghanistan'}]
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % p.join(BASEDIR, DB_NAME)
    API_LIMIT = 1000
    SW = False
    DEBUG = False
    TESTING = False
    PROD = False
    CHUNK_SIZE = 2 ** 14
    ROW_LIMIT = None
    LOGFILE = p.join(BASEDIR, 'http', 'log.txt')


class Scraper(Config):
    PROD = True
    SW = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % p.join(PARENTDIR, DB_NAME)
    LOGFILE = p.join(PARENTDIR, 'http', 'log.txt')


class Production(Config):
    PROD = True


class Development(Config):
    DEBUG = True
    CHUNK_SIZE = 2 ** 4
    ROW_LIMIT = 50


class Test(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True
    CHUNK_SIZE = 2 ** 4
    ROW_LIMIT = 10
    TESTING = True
