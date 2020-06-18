# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-15 07:56:42
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-18 11:28:56
import datetime

import pytest
from django.apps import apps
from django.conf import settings
from django.contrib.gis.geos import Point

from mydineout.profile.models import Profile
from mydineout.restaurant.models import Restaurant

pytestmark = pytest.mark.django_db


def test_restaurant_model():
    opening_time = datetime.time(10, 00, 00)
    closing_time = datetime.time(23, 00, 00)
    restaurant_obj = Restaurant.objects.create(name_of_the_restaurant='Test',
                                               opening_time=opening_time,
                                               closing_time=closing_time, menu='Thai',
                                               city='Gurugram', pincode='122018',
                                               location=Point(76.9220, 28.3952, srid=4326))
    assert restaurant_obj.name_of_the_restaurant == 'Test'
    assert restaurant_obj.opening_time == opening_time
    assert restaurant_obj.closing_time == closing_time
    assert restaurant_obj.menu == 'Thai'
    assert restaurant_obj.city == 'Gurugram'
    assert restaurant_obj.pincode == '122018'
    assert restaurant_obj.location == Point(76.9220, 28.3952, srid=4326)
    assert str(restaurant_obj) == 'Test'


def test_profile_model():
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user_instance = User.objects.create(username='abcd', password='1234',
                                        first_name='sakshi', last_name='gandhi')
    user_instance.save()
    profile = Profile.objects.create(user=user_instance, bio='Test Bio', city='Dehradun',
                                     country='India', postal_code='248001',
                                     birth_date=datetime.date(1992, 6, 13))
    assert profile.user == user_instance
    assert profile.bio == 'Test Bio'
    assert profile.country == 'India'
    assert profile.postal_code == '248001'
    assert profile.birth_date.strftime('%Y-%m-%d') == '1992-06-13'
    assert str(profile) == 'abcd'
