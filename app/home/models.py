# encoding: utf8
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name')
    description = models.TextField(blank=True, verbose_name='Description')
    date_created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(verbose_name='The time of notification')
    end_time = models.DateTimeField(verbose_name='The expiry time of notification')
    warning_time = models.IntegerField(verbose_name='The time for warning before of notification')
    color = models.CharField(verbose_name='Color for this task', max_length=7, blank=True)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
