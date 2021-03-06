# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 17:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=30, validators=[django.core.validators.RegexValidator(message='Incorrect format, please enter your phone number correctly', regex='^\\+?1?\\d{9,15}$')])),
                ('subject', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(blank=True, max_length=30, validators=[django.core.validators.RegexValidator(message='Incorrect format, please enter your phone number correctly', regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
    ]
