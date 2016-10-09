# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-22 09:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160920_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='length',
        ),
        migrations.AddField(
            model_name='task',
            name='color',
            field=models.CharField(blank=True, max_length=7, verbose_name='Color for this task'),
        ),
        migrations.AddField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 9, 4, 32, 987354, tzinfo=utc), verbose_name='The expiry time of notification'),
            preserve_default=False,
        ),
    ]