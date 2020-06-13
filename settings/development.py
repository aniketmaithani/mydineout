# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-14 03:04:31
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-14 03:33:44
from .settings import *

INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar', 'django_extensions', ]

MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = ('127.0.0.1',)