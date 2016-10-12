from django.db import models
from app.user.models import UserProfile
from datetime import datetime


class Word(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name='Word', max_length=128)
    description = models.TextField(verbose_name='Description', max_length=2000)

    def __str__(self):
        return self.name


class Settings(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.TimeField(verbose_name='Start time for the notifications')
    end_time = models.TimeField(verbose_name='End time for the notifications')
    range = models.IntegerField(verbose_name='The time of appearance of new words / min.')
    last_request = models.TimeField(blank=True)
    number_word = models.IntegerField(default=1)

    def __str__(self):
        return 'Settings'
