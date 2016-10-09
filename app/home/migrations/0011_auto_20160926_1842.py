# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-26 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20160926_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='repeat',
            field=models.CharField(choices=[('never', 'never'), ('1day', '1 day'), ('2day', '2 days'), ('1wk', '1 week'), ('2wks', '2 weeks'), ('mn', 'month'), ('yr', 'year')], default='never', max_length=10, verbose_name='The retry time of the event'),
        ),
    ]