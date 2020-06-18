# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-18 11:30:03
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-18 13:12:25
import datetime
import random

import pytest
from django.contrib.auth import authenticate
from django.contrib.gis.geos import Point
from rest_framework.authtoken.models import Token

from mydineout.profile.models import Profile
from mydineout.restaurant.models import Restaurant

from .. import factories as f


@pytest.mark.django_db
def test_restaurant_distance(client):
    menu = ['Thai', 'Chinese', 'Continental', 'Indian', 'Japanese']
    long = 77.0752
    lat = 28.4024

    # Create User
    user_obj = f.create_user(username='shiprasharma', password='test123')
    user_obj.save()

    # Trying Out User Creds
    user_authenticate = authenticate(
        username='shiprasharma', password='test123')
    Token.objects.get_or_create(user=user_authenticate)
    token_value = str(user_authenticate.auth_token)

    # Create Profile
    Profile.objects.create(user=user_authenticate, bio='Test Bio', city='Dehradun',
                           country='India', postal_code='248001',
                           birth_date=datetime.date(1992, 6, 13))
    # Create Multiple Restaurants
    for _ in range(4):
        opening_time = datetime.time(10, 00, 00)
        closing_time = datetime.time(23, 00, 00)

        Restaurant.objects.create(name_of_the_restaurant="Restaurant-{}".format(_),
                                  opening_time=opening_time,
                                  closing_time=closing_time,
                                  menu=menu[random.randint(0, 4)],
                                  city='Gurugram',
                                  country='India', pincode='122018',
                                  location=Point(long, lat, srid=4326))
        lat = lat + 2
        long = long + 2

    lat_long_one = [74.0752, 24.4024]
    lat_long_two = [104.0752, 40.4024]
    url = '/api/v1/restaurant/fromdistance?lat={}&long={}'.format(
        lat_long_one[0], lat_long_one[1])
    response = client.get(
        url, HTTP_AUTHORIZATION='Token {}'.format(token_value))
    assert response.status_code == 200
    # A per lat_long_one should include all restaurant
    assert len(response.json()) == 4

    # In this case Restaurant-3 should be nearest
    url = '/api/v1/restaurant/fromdistance?lat={}&long={}'.format(
        lat_long_two[0], lat_long_two[1])
    response = client.get(
        url, HTTP_AUTHORIZATION='Token {}'.format(token_value))
    assert response.status_code == 200
    assert len(response.json()) == 4
