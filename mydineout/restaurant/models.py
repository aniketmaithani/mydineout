# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-12 16:49:14
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-12 16:59:27
from django.contrib.gis.db.models import PointField
from django.db import models


class Restaurant(models.Model):
    name_of_the_restaurant = models.CharField(max_length=30, blank=True)
    opening_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)
    menu = models.TextField(blank=True, null=False, help_text='Menu of the Restaurant')
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    pincode = models.CharField(max_length=30, blank=True)
    location = PointField(srid=4326, geography=True, blank=True, null=True)

    def __str__(self):
        return self.name_of_the_restaurant
