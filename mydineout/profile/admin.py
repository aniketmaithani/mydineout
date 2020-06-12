# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-12 15:44:42
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-12 15:55:48
from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'country', 'postal_code')
    ordering = ('user',)
    search_fields = ('user__username', 'city', 'country', 'postal_code')

    def user(self, obj):
        return obj.username
    user.admin_order_field = 'user'
    user.short_description = 'User Name'


admin.site.register(Profile, ProfileAdmin)
