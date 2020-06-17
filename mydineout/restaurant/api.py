# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-14 06:44:25
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-16 05:50:04
from django.db.models import Q
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .helper import blacklisted_restaurant, get_restaurant_by_distance
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
                Q(city=city) | Q(pincode=postal_code))
        if country and city is not None and postal_code is None:
            queryset = Restaurant.objects.filter(country=country, city=city)
        return queryset

    def get(self, request, format=None):
        restaurant_qs = self.get_queryset()
        blacklist_res_qs = blacklisted_restaurant(
            restaurant_qs, self.request.user)
        filter_out_blacklisted = restaurant_qs.difference(blacklist_res_qs)
        serializer = RestaurantSerializer(filter_out_blacklisted, many=True,
                                          context={'request': self.request})
        return Response(serializer.data)


@api_view(['GET'])
def get_restaurant_from_reference_point(request):
    if request.method == 'GET':
        user_latitude = request.query_params.get('lat', None)
        user_longitude = request.query_params.get('long', None)
        qs = get_restaurant_by_distance(
            user_longitude, user_latitude, request.user)
        serializer = RestaurantSerializer(
            qs, many=True, context={'request': request})
        return Response(serializer.data)
