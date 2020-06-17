# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-17 17:18:24
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-17 18:03:27
import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from mydineout.profile.models import Profile


class Command(BaseCommand):
    help = 'Create dummy users as test data'

    def handle(self, *args, **options):
        faker = Faker()
        for _ in range(3):
            name_of_user = faker.name()
            first_name = name_of_user.split()[0]
            last_name = name_of_user.split()[1]
            user_obj = User.objects.create(username=name_of_user,
                                           email=faker.email(),
                                           password='test123',
                                           first_name=first_name,
                                           last_name=last_name)
            Profile.objects.create(user=user_obj,
                                   bio=faker.text(),
                                   city='Gurugram',
                                   postal_code='122018',
                                   birth_date=datetime.date(1991, 10, 18))

        self.stdout.write(self.style.SUCCESS('Added 3 users to DB'))
