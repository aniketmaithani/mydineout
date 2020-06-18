# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-17 18:52:16
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-17 18:52:19
from django.apps import apps
from django.conf import settings
from django_dynamic_fixture import G


def create_user(**kwargs):
    """Create an user along with their dependencies."""
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = G(User, **kwargs)
    user.set_password(kwargs.get("password", "test"))
    user.save()
    return user
