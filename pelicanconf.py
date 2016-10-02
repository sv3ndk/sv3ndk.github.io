#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Svend Vanderveken'
SITENAME = u"Svend's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        )

# Social widget
SOCIAL = (
         ("Svend's Github profile", 'https://github.com/svendx4f'),
     	 ("Svend's Twitter feed", 'https://twitter.com/svend_x4f'),
     	 ("Svend's LinkedIn profile", 'https://be.linkedin.com/in/vanderveken'),
     	 ("Svend's StackOverflow profile", 'http://stackoverflow.com/users/3318335/svend'),
          )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = [ 'ipynb.markup']

IGNORE_FILES = [".ipynb_checkpoints"]

