# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-20 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160920_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='The amount of time for this task'),
        ),
    ]