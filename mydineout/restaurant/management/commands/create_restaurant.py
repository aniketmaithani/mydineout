# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-17 17:18:24
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-17 17:37:34
import datetime
import random

from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from faker import Faker

from mydineout.restaurant.models import Restaurant


class Command(BaseCommand):
    help = 'Create dummy data for restaurant'

    def handle(self, *args, **options):
        faker = Faker()
        menu = ['Thai', 'Chinese', 'Continental', 'Indian', 'Japanese']
        long = 77.0752
        lat = 28.4024
        for _ in range(10):
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

        self.stdout.write(self.style.SUCCESS('Added 10 restaurant to DB'))
