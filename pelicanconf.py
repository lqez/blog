#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#AUTHOR = u"lqez"
EMAIL = "ez.amiryo@gmail.com"
SITENAME = u"Feature creep designer"
#SITEURL = '//lqez.github.io/blog'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'
THEME = '42signals-pelican-theme'

# Social widget
#LINKS = (('twitter', 'http://twitter.com/lqez'),
#          ('facebook', 'http://facebook.com/ez.amiryo'),
#          ('soundcloud', 'http://soundcloud.com/lqez'),
#          ('github', 'http://github.com/lqez'),)
#
#SOCIAL = (('twitter', 'http://twitter.com/lqez'),
#          ('facebook', 'http://facebook.com/ez.amiryo'),
#          ('soundcloud', 'http://soundcloud.com/lqez'),
#          ('github', 'http://github.com/lqez'),)

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
