from datetime import datetime

from app.home.models import Task
from app.push_message.functions import push_message
from app.push_message.models import AwaitingDelivery
from celery import shared_task
from conf.settings import SEP


def get_events_today():
    date = datetime.today().date()
    time = datetime.today().time()

    objects = Task.objects.exclude(last_request=date)
    answer = objects.filter(repeat='never').filter(date_notice=date)
    answer |= objects.filter(repeat='1day')

    for i in objects.filter(repeat='2day'):
        if (date - i.date_notice).days % 2 == 0:
            answer |= objects.filter(pk=i.pk)
    for i in objects.filter(repeat='1wk'):
        if (date - i.date_notice).days % 7 == 0:
            answer |= objects.filter(pk=i.pk)
    for i in objects.filter(repeat='2wks'):
        if (date - i.date_notice).days % 14 == 0:
            answer |= objects.filter(pk=i.pk)
    answer |= objects.filter(repeat='mn').filter(date_notice__day=date.day)
    answer |= objects.filter(repeat='yr').filter(date_notice__month=date.month).filter(date_notice__day=date.day)

    answer = answer.filter(time_notice__lte=time)
    return answer


@shared_task()
def check_current_event():
    date = datetime.today()

    # the resulting data is relevant for today and current time
    tasks = get_events_today()
    print("********** Check current event ***********")
    for i in tasks:
        token = i.user.token
        username = i.user.name
        for one_token in token.split(SEP):
            a = AwaitingDelivery.objects.create(task=i, token=one_token)
            push_message(username, one_token, a.pk)
        i.last_request = date
        i.save()
