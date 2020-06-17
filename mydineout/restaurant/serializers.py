# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-14 06:40:06
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-16 06:11:08
from rest_framework import serializers

from .helper import is_favourite_restaurant, is_open
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()
    is_open = serializers.SerializerMethodField()

    def get_is_favourite(self, obj):
        return is_favourite_restaurant(obj.id, self.context['request'].user)

    def get_is_open(self, obj):
        return is_open(obj)

    class Meta:
        model = Restaurant
        fields = ('name_of_the_restaurant', 'opening_time',
                  'closing_time', 'city', 'pincode', 'location', 'is_favourite',
                  'is_open')
