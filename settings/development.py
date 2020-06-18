# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-14 03:04:31
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-18 12:37:36
from .settings import *  # noqa

INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar', 'django_extensions', ]  # noqa

MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware', ]  # noqa

INTERNAL_IPS = ('127.0.0.1',)  # noqa
