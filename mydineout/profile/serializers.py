# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-15 17:21:10
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-15 20:32:18
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
