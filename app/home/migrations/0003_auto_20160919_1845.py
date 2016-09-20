# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-19 18:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160919_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 19, 18, 44, 22, 138412, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 19, 18, 44, 30, 243105, tzinfo=utc), verbose_name='The time expiration of notification'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='adfdfd', max_length=128, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 19, 18, 44, 56, 972212, tzinfo=utc), verbose_name='The time of notification'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='warning_time',
            field=models.IntegerField(default=10, verbose_name='The time for warning before of notification'),
            preserve_default=False,
        ),
    ]