from datetime import date

from app.home.models import Task
from app.push_message.functions import push_message
from app.push_message.models import AwaitingDelivery
from celery import shared_task
from conf.settings import SEP
from .views import get_events_today


@shared_task()
def check_current_event():
    tasks = get_events_today(date.today(), (Task.objects.exclude(last_request=date.today())))
    print("********** Check current event ***********")
    for i in tasks:
        token = i.user.token
        username = i.user.name
        for one_token in token.split(SEP):
            a = AwaitingDelivery.objects.create(task=i, token=one_token)
            push_message(username, one_token, a.pk)
        i.last_request = date.today()
        i.save()
