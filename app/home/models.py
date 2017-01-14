# encoding: utf8
from datetime import datetime

from django.db import models

from app.user.models import UserProfile

PERIODS = [
    ('never', 'Never'),
    ('1day', 'Every day'),
    ('2day', 'In 2 days'),
    ('1wk', 'Every week'),
    ('2wks', 'In 2 weeks'),
    ('mn', 'Every month'),
    ('yr', 'Every year')
]
COLORS = [
    ('#000000', 'Black'),
    ('#FF0000', 'Red'),
    ('#00FF00', 'Lime'),
    ('#0000FF', 'Blue'),
    ('#FFFFFF', 'White'),
    ('#00FFFF', 'Aqua'),
    ('#FF00FF', 'Fuchsia'),
    ('#FFFF00', 'Yellow'),

]


class Task(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='task_user')
    name = models.CharField(max_length=128, verbose_name='Name')
    description = models.TextField(blank=True, verbose_name='Description')
    date_created = models.DateTimeField(auto_now_add=True)

    date = models.DateField(verbose_name='Date of event', blank=True, null=True)
    start = models.TimeField(verbose_name='Time of event', blank=True, null=True)
    end = models.TimeField(verbose_name='Expiry time of event', blank=True, null=True)

    time_notice = models.TimeField(verbose_name='Time of notification', blank=True, null=True)
    date_notice = models.DateField(verbose_name='Date of notification', blank=True, null=True)
    repeat = models.CharField(max_length=10, verbose_name='Retry time of the event', choices=PERIODS,
                              default=PERIODS[0][0])
    last_request = models.DateField(verbose_name="Last query time", default=datetime(1960, 1, 1))
    color = models.CharField(verbose_name='Color for this task', max_length=7, choices=COLORS,
                             default=COLORS[0][0])
    notice = models.BooleanField(verbose_name='Notice', default=False)

    def clean(self):
        if None in (self.date, self.start, self.end, self.time_notice, self.date_notice):
            self.notice = True
        else:
            self.notice = False
        return

    def __str__(self):
        return self.name

    @property
    def full_datetime(self):
        if self.notice:
            return
        return datetime.combine(self.date, self.start)

    def is_request_today(self):
        return True if self.last_request == datetime.today().date() else False
    is_request_today.boolean = True
