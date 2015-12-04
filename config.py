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

import itertools as it

from os import path as p

BASEDIR = p.dirname(__file__)
PARENTDIR = p.dirname(BASEDIR)
DB_NAME = 'scraperwiki.sqlite'
RECIPIENT = 'reubano@gmail.com'


class Config(object):
    BASE_URL = 'http://sdwebx.worldbank.org/climateportal/components/getData.cfc'
    SUB_QUERY = {
        'thisSYear': 1990,
        'thisEYear': 2012,
        'thisLevel': 'country'}

    BASE_QUERY = {
        'method': 'getCCKHistoricalMonthlyCRUChart',
        'returnFormat': 'json',
        '_cf_nodebug': 'true',
        '_cf_nocache': 'true',
        '_cf_rc': 5}

    codes = {
        'DZA': 'Algeria',
        'AGO': 'Angola',
        'SHN': 'Ascension',
        'BEN': 'Benin',
        'BWA': 'Botswana',
        'BFA': 'Burkina Faso',
        'BDI': 'Burundi',
        'CMR': 'Cameroon',
        'CPV': 'Cape Verde Islands',
        'CAF': 'Central African Republic',
        'TCD': 'Chad Republic',
        'COM': 'Comoros',
        'COG': 'Congo',
        'DJI': 'Djibouti',
        'EGY': 'Egypt',
        'GNQ': 'Equatorial Guinea',
        'ERI': 'Eritrea',
        'ETH': 'Ethiopia',
        'GAB': 'Gabon Republic',
        'GMB': 'Gambia',
        'GHA': 'Ghana',
        'GNB': 'Guinea-Bissau',
        'GIN': 'Guinea',
        'CIV': 'Ivory Coast',
        'KEN': 'Kenya',
        'LSO': 'Lesotho',
        'LBR': 'Liberia',
        'LBY': 'Libya',
        'MDG': 'Madagascar',
        'MWI': 'Malawi',
        'MLI': 'Mali Republic',
        'MRT': 'Mauritania',
        'MUS': 'Mauritius',
        'MYT': 'Mayotte Island',
        'MAR': 'Morocco',
        'MOZ': 'Mozambique',
        'NAM': 'Namibia',
        'NER': 'Niger Republic',
        'NGA': 'Nigeria',
        'STP': 'Principe',
        'REU': 'Reunion Island',
        'RWA': 'Rwanda',
        'STP': 'Sao Tome',
        'SEN': 'Senegal Republic',
        'SYC': 'Seychelles',
        'SLE': 'Sierra Leone',
        'SOM': 'Somalia Republic',
        'ZAF': 'South Africa',
        'SHN': 'St. Helena',
        'SDN': 'Sudan',
        'SWZ': 'Swaziland',
        'TZA': 'Tanzania',
        'TGO': 'Togo',
        'TUN': 'Tunisia',
        'UGA': 'Uganda',
        'COD': 'Zaire',
        'ZMB': 'Zambia',
        'TZA': 'Zanzibar',
        'ZWE': 'Zimbabwe',
        'SSD': 'South Sudan',
        'COD': 'Dem. Republic of the Congo'}

    metrics = {
        'tas': 'Average monthly temperature from 1990-2012',
        'pr': 'Average monthly rainfall from 1990-2012'}

    args = it.product(codes.items(), metrics.items())

    TABLES = [
        {
            'name': 'climate', 'rid': 'rid', 'code': a[0][0],
            'country': a[0][1], 'metric': a[1][0], 'description': a[1][1]}
        for a in args]

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
    ROW_LIMIT = 16


class Test(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True
    CHUNK_SIZE = 2 ** 4
    ROW_LIMIT = 10
    TESTING = True
