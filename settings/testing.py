# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-14 14:50:48
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-18 09:16:07
from .development import *

MEDIA_ROOT = "/tmp"

SECRET_KEY = "itsmykeyandidontwanttoshareitokay"

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'test',
        'USER': 'aniketmaithani',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

INSTALLED_APPS += ("tests",)

ALLOWED_HOSTS = ['127.0.0.1']
