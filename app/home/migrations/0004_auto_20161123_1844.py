# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-23 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0003_auto_20161123_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='only_notice',
            new_name='notice',
        ),
    ]