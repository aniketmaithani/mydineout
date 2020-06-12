# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-12 16:58:21
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-12 16:59:48
from django.contrib import admin

from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name_of_the_restaurant', 'city', 'country', 'menu', 'location')
    ordering = ('name_of_the_restaurant', 'city', 'country')
    search_fields = ('name_of_the_restaurant', 'city', 'country', 'pincode')


admin.site.register(Restaurant, RestaurantAdmin)
