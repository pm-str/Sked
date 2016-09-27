# encoding: utf8
from django.db import models


class Task(models.Model):
    PERIODS = [
        ('never', 'never'),
        ('1day', '1 day'),
        ('2day', '2 days'),
        ('1wk', '1 week'),
        ('2wks', '2 weeks'),
        ('mn', 'month'),
        ('yr', 'year')
    ]
    name = models.CharField(max_length=128, verbose_name='Name')
    description = models.TextField(blank=True, verbose_name='Description')
    date_created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(verbose_name='The date of notification')
    start_time = models.TimeField(verbose_name='The time of notification')
    end_time = models.TimeField(verbose_name='The expiry time of notification')
    warning_time = models.IntegerField(verbose_name='The time for warning before of notification')
    repeat = models.CharField(max_length=10, verbose_name='The retry time of the event', choices=PERIODS,
                              default=PERIODS[0][0])
    color = models.CharField(verbose_name='Color for this task', max_length=7, blank=True)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
