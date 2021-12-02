#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#AUTHOR = u"lqez"
EMAIL = "ez.amiryo@gmail.com"
SITENAME = "Feature creep designer"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
#SITEURL = '//lqez.github.io/blog'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'
THEME = './themes/42signals-pelican-theme'

MARKUP = ('md',)
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {'baselevel': 2, 'toc_depth': '2-5'},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

DEFAULT_PAGINATION = 5
STATIC_PATHS = ["images", ]

PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    'pelican-embed-tweet.embed_tweet',
    #'pelican-check-ext-link',
]
