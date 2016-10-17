# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-17 08:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='color',
            field=models.CharField(choices=[('#000000', 'Black'), ('#FF0000', 'Red'), ('#00FF00', 'Lime'), ('#0000FF', 'Blue'), ('#FFFFFF', 'White'), ('#00FFFF', 'Aqua'), ('#FF00FF', 'Fuchsia'), ('#FFFF00', 'Yellow')], default='#000000', max_length=7, verbose_name='Color for this task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(verbose_name='Date of event'),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.TimeField(verbose_name='Expiry time of event'),
        ),
        migrations.AlterField(
            model_name='task',
            name='last_request',
            field=models.DateField(default=datetime.datetime(1960, 1, 1, 0, 0), verbose_name='Last query time'),
        ),
        migrations.AlterField(
            model_name='task',
            name='repeat',
            field=models.CharField(choices=[('never', 'Never'), ('1day', 'Every day'), ('2day', 'In 2 days'), ('1wk', 'Every week'), ('2wks', 'In 2 weeks'), ('mn', 'Every month'), ('yr', 'Every year')], default='never', max_length=10, verbose_name='Retry time of the event'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.TimeField(verbose_name='Time of event'),
        ),
    ]
