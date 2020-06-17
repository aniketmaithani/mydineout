# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-15 14:57:02
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-17 14:52:27
import datetime

from django.contrib.gis.db.models.functions import GeometryDistance
from django.contrib.gis.geos import Point

from mydineout.profile.models import Profile
from mydineout.restaurant.models import Restaurant


def is_favourite_restaurant(restaurant_id, user):
    favourite_restaurant_qs = Profile.objects.get(
        user=user).favourite_restaurant.filter(
        pk=restaurant_id).exists()
    return favourite_restaurant_qs


def blacklisted_restaurant(restaurant_qs, user):
    blacklisted_restaurant_qs = Profile.objects.get(
        user=user).blacklisted_restaurant.filter(
        pk__in=restaurant_qs.values_list('id', flat=True))
    return blacklisted_restaurant_qs


def blacklist_restaurant_by_id(id_, user):
    restaurant_obj = Restaurant.objects.get(pk=id_)
    profile_obj = Profile.objects.get(user=user)
    profile_obj.blacklisted_restaurant.add(restaurant_obj)
    response = {'Success': 'Restaurant has been blacklisted'}
    return response


def mark_favourite_restaurant_by_id(id_, user):
    restaurant_obj = Restaurant.objects.get(pk=id_)
    profile_obj = Profile.objects.get(user=user)
    profile_obj.favourite_restaurant.add(restaurant_obj)
    response = {'Success': 'Restaurant has been marked as favourite'}
    return response


def get_restaurant_by_distance(user_long, user_lat, user):
    user_reference_point = Point(float(user_long), float(user_lat), srid=4326)
    restaurant_by_distance_qs = Restaurant.objects.annotate(
        distance=GeometryDistance('location', user_reference_point)
    ).order_by('distance')
    blacklist_res_qs = blacklisted_restaurant(restaurant_by_distance_qs, user)
    blacklist_with_distance_annotation = blacklist_res_qs.annotate(
        distance=GeometryDistance('location',
                                  user_reference_point)).order_by('distance')
    restaurant_qs = restaurant_by_distance_qs.difference(
        blacklist_with_distance_annotation)
    return restaurant_qs


def is_open(obj):
    current_time = datetime.datetime.now().time()
    if current_time < obj.closing_time:
        return True
    else:
        return False
