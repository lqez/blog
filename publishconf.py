#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://lqez.github.io/blog'
PLUGINS = ['pelican.plugins.embed_tweet',]

RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

APPLE_TOUCH_ICON = 'fcd-57.png'
APPLE_TOUCH_ICON_72 = 'fcd-72.png'
APPLE_TOUCH_ICON_114 = 'fcd-114.png'

GOOGLE_ANALYTICS = 'UA-37711911-1'

FACEBOOK_APPID = '465940413466203'
FACEBOOK_LOCALE = 'ko_KR'

FACEBOOK_COMMENT = True
FACEBOOK_COMMENT_NUM_POST = 5
FACEBOOK_COMMENT_WIDTH = 0
