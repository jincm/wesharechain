#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import logging

STATIC_PATH = os.path.join(os.path.dirname(os.path.normpath(__file__)), 'static')
TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.normpath(__file__)), 'templates')

default_settings = {
    'base_url': '/',
    'view_prefix': '/block',
    'api_version': 'v1.0',
    'enabled_methods': ['get', 'post', 'put', 'patch', 'delete'],
    'log_info': "./log/block_info.log",
    'log_error': "./log/block_error.log",
    'static_path': STATIC_PATH,
    'commodity_path': '/image/commodity/'
}

models = []

Debug = False

if Debug:
    logging.basicConfig(level=logging.DEBUG)
