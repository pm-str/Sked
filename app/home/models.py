# encoding: utf8
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name')
    description = models.TextField(blank=True, verbose_name='Description')
    date_created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(verbose_name='The time of notification')
    length = models.DecimalField(verbose_name='The amount of time for this task', max_digits=20, decimal_places=2)
    warning_time = models.IntegerField(verbose_name='The time for warning before of notification')

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
