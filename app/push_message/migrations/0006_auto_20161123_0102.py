# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-23 01:02
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('push_message', '0005_auto_20161123_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awaitingdelivery',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 23, 1, 2, 29, 174376)),
        ),
    ]
