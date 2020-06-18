# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-17 19:36:46
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-18 11:03:52
import datetime
import json

import pytest
from django.contrib.auth import authenticate
from django.contrib.gis.geos import Point
from rest_framework.authtoken.models import Token

from mydineout.profile.models import Profile
from mydineout.restaurant.models import Restaurant

from .. import factories as f


@pytest.mark.django_db
def test_blacklist_restaurant(client):
    user_obj = f.create_user(username='blacklist', password='test123')
    user_obj.save()
    user_creds = {"username": "blacklist", "password": "test123"}
    user_authenticate = authenticate(username='blacklist', password='test123')
    Token.objects.get_or_create(user=user_authenticate)
    # Create Profile
    Profile.objects.create(user=user_authenticate, bio='Test Bio', city='Dehradun',
                           country='India', postal_code='248001',
                           birth_date=datetime.date(1992, 6, 13))
    token_login_url = '/api/v1/auth/token/login'
    response = client.json.post(token_login_url, json.dumps(user_creds))
    assert response.status_code == 200
    assert 'auth_token' in response.json()
    assert response.json()['auth_token'] == str(user_authenticate.auth_token)
    token_value = str(user_authenticate.auth_token)
    opening_time = datetime.time(10, 00, 00)
    closing_time = datetime.time(23, 00, 00)
    long = 77.0752  # Reference for Restaurant
    lat = 28.4024  # Reference for Restaurant
    restaurant_obj = Restaurant.objects.create(name_of_the_restaurant='Test Restaurant',
                                               opening_time=opening_time,
                                               closing_time=closing_time,
                                               menu='Thai',
                                               city='Gurugram',
                                               country='India', pincode='122018',
                                               location=Point(long, lat, srid=4326))
    restaurant_obj.save()
    url = '/api/v1/restaurant/blacklistrestaurant?rid={}'.format(
        restaurant_obj.id)
    response_for_blacklist_url = client.get(
        url, HTTP_AUTHORIZATION='Token {}'.format(token_value))
    assert response_for_blacklist_url.status_code == 200
