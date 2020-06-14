# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-14 06:44:25
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-14 12:01:13
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = {'Error': 'Please pass valid url parameters'}
        city = self.request.query_params.get('city', None)
        postal_code = self.request.query_params.get('postalcode', None)
        country = self.request.query_params.get('country', None)
        if city is not None or postal_code is not None:
            queryset = Restaurant.objects.filter(
                Q(city=city) | Q(pincode=postal_code), country=country)
        return queryset

    def get(self, request, format=None):
        restaurant_qs = self.get_queryset()
        serializer = RestaurantSerializer(restaurant_qs, many=True)
        return Response(serializer.data)
