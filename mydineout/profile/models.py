# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-12 15:41:38
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-12 15:44:10
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    postal_code = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
