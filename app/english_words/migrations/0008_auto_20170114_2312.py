# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-14 16:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('english_words', '0007_auto_20170114_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='created_date',
        ),
        migrations.AddField(
            model_name='word',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 1, 14, 16, 12, 10, 924243, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
