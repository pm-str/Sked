from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery_tasks' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('celery_tasks', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'app.celery_tasks.celery.check_event',
        'schedule': 30.0
    },
    'check-every-30-seconds': {
        'task': 'app.celery_tasks.celery.clear_queue',
        'schedule': crontab()
    },
}


@app.task
def clear_queue():
    from app.push_message.functions import clear_queue
    clear_queue()


@app.task
def check_event():
    from app.home.tasks import check_current_event
    from app.english_words.tasks import check_current_word
    check_current_event()
    check_current_word()