# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-17 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('english_words', '0009_auto_20170116_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='end_time',
            field=models.TimeField(verbose_name='Не уведомлять после'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='last_request',
            field=models.TimeField(blank=True, verbose_name='Последнее оповещение'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='number_word',
            field=models.IntegerField(default=1, verbose_name='Текущая позиция слова'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='range',
            field=models.IntegerField(verbose_name='Промежуток появления новых слов'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='start_time',
            field=models.TimeField(verbose_name='Время начала уведомлений'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='word',
            name='last_request',
            field=models.DateTimeField(auto_now=True, verbose_name='Last request'),
        ),
    ]
