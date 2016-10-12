from django.db import models
from app.home.models import Task
from app.english_words.models import Word


class AwaitingDelivery(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Message'
