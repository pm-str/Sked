from django.db import models

from app.user.models import UserProfile


class Word(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name='Word', max_length=128)
    transcription = models.CharField(verbose_name='Transcription', max_length=128, blank=True)
    translation = models.TextField(verbose_name='Translation', max_length=1000)
    example = models.TextField(verbose_name='Example', max_length=1000, blank=True)
    last_request = models.DateTimeField(auto_now=True, verbose_name='Last request')
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Settings(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    start_time = models.TimeField(verbose_name='Время начала уведомлений')
    end_time = models.TimeField(verbose_name='Не уведомлять после')
    range = models.IntegerField(verbose_name='Промежуток появления новых слов')
    last_request = models.TimeField(verbose_name='Последнее оповещение', blank=True)
    number_word = models.IntegerField(default=1, verbose_name='Текущая позиция слова')

    def __str__(self):
        return 'Настройки'

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

