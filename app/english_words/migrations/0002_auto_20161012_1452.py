# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-12 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('english_words', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile'),
        ),
    ]
