from app.english_words.models import Word
from app.home.models import Task
from django.db import models


class AwaitingDelivery(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    token = models.CharField(verbose_name="Recipient's token", max_length=1000, blank=True)

    def __str__(self):
        return self.datetime.isoformat(sep=' ')[:19]
