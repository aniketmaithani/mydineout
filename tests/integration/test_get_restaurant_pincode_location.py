# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-18 11:11:06
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-18 11:26:19
import datetime
import random

import pytest
from django.contrib.auth import authenticate
from django.contrib.gis.geos import Point
from faker import Faker
from rest_framework.authtoken.models import Token

from mydineout.profile.models import Profile
from mydineout.restaurant.models import Restaurant

from .. import factories as f


@pytest.mark.django_db
def test_get_restaurant(client):
    faker = Faker()
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

        Restaurant.objects.create(name_of_the_restaurant=faker.company(),
                                  opening_time=opening_time,
                                  closing_time=closing_time,
                                  menu=menu[random.randint(0, 4)],
                                  city='Gurugram',
                                  country='India', pincode='122018',
                                  location=Point(long, lat, srid=4326))
        lat = lat + 2
        long = long + 2

    test_list_one = ['122018', 'Gurugram', 'India']
    test_list_two = ['248001', 'Gurugram', 'India']
    test_list_three = ['248001', 'Dehradun', 'Iceland']
    url = '/api/v1/restaurant/getrestaurant?pincode={}&city={}&country={}'.format(
        test_list_one[0], test_list_one[1], test_list_one[2])
    response = client.get(
        url, HTTP_AUTHORIZATION='Token {}'.format(token_value))
    assert response.status_code == 200
    # A per test_list_one should include all restaurant
    assert len(response.json()) == 4
    url = '/api/v1/restaurant/getrestaurant?pincode={}&city={}&country={}'.format(
        test_list_two[0], test_list_two[1], test_list_two[2])
    response = client.get(
        url, HTTP_AUTHORIZATION='Token {}'.format(token_value))
    assert response.status_code == 200
    assert len(response.json()) == 4
    url = '/api/v1/restaurant/getrestaurant?pincode={}&city={}&country={}'.format(
        test_list_three[0], test_list_three[1], test_list_three[2])
    response = client.get(
        url, HTTP_AUTHORIZATION='Token {}'.format(token_value))
    assert response.status_code == 200
    assert 'Message' in response.json()  # Since Country param doesn't match
