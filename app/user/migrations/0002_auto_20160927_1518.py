# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-27 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='token',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
