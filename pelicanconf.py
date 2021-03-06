#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'lapis_zero09'
SITENAME = '題未定'
SITEURL = 'https://www.lapis-zero09.xyz'
# SITEURL = 'http://localhost:8000'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'
PATH = 'content'

PROFILE_IMG_URL = './img/profile.jpg'
THEME = './pure-single/'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['render_math']
macros = ['./latex-macros.tex']
MATH_JAX = {'color': '', 'align': 'centor', 'macros': macros}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/lapis-zero09'),
    ('rss-square', 'http://lapis-zero09.hatenablog.com/'),
    ('gift', 'http://amzn.asia/8plng3k'),
    ('search', 'http://qiita.com/lapis_zero09')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
