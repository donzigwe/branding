# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-27 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brandid', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='description',
        ),
    ]
