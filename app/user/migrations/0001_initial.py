# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-11 17:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars')),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField(blank=True)),
                ('token', models.CharField(blank=True, max_length=512)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
