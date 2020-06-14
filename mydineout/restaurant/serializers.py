# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-14 06:40:06
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-14 06:44:07
from rest_framework import serializers

from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'name_of_the_restaurant', 'menu', 'city', 'country', 'pincode']
