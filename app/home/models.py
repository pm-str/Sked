# encoding: utf8
from django.db import models
from app.user.models import UserProfile


class Task(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='task_user')
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
    date = models.DateField(verbose_name='The date of event')
    start = models.TimeField(verbose_name='The time of event')
    end = models.TimeField(verbose_name='The expiry time of event')
    time_notice = models.TimeField(verbose_name='Time of notification')
    date_notice = models.DateField(verbose_name='Date of notification')
    repeat = models.CharField(max_length=10, verbose_name='The retry time of the event', choices=PERIODS,
                              default=PERIODS[0][0])
    last_request = models.DateField(verbose_name="It's the time of the last query to this task", blank=True)
    color = models.CharField(verbose_name='Color for this task', max_length=7, blank=True)

    def __str__(self):
        return self.name


class AwaitingDelivery(models.Model):
    queue = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.queue.name
