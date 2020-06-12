# Generated by Django 3.0.7 on 2020-06-12 11:30

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_restaurant', models.CharField(blank=True, max_length=30)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('menu', models.TextField(blank=True, help_text='Menu of the Restaurant')),
                ('city', models.CharField(blank=True, max_length=30)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('pincode', models.CharField(blank=True, max_length=30)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
            ],
        ),
    ]
