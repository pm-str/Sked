from datetime import datetime, date
from app.home.models import Task
from app.push_message.models import AwaitingDelivery
from celery import shared_task
from app.push_message.send import push_message
from conf.settings import SEP


def get_notice_today(events):
    today = date.today()
    objects = events.objects.exclude(last_request=today)

    answer = objects.filter(repeat='never').filter(date_notice=today)
    answer |= objects.filter(repeat='1day')
    for i in objects.filter(repeat='2day'):
        if (today - i.date_notice).days % 2 == 0:
            answer |= objects.filter(pk=i.pk)
    for i in objects.filter(repeat='1wk'):
        if (today - i.date_notice).days % 7 == 0:
            answer |= objects.filter(pk=i.pk)
    for i in objects.filter(repeat='2wks'):
        if (today - i.date_notice).days % 14 == 0:
            answer |= objects.filter(pk=i.pk)
    answer |= objects.filter(repeat='mn').filter(date_notice__day=today.day)
    answer |= objects.filter(repeat='yr').filter(date_notice__month=today.month).filter(date_notice__day=today.day)

    answer = answer.filter(time_notice__lte=datetime.today().time())
    return answer


@shared_task()
def check_current_event():
    tasks = get_notice_today(Task)
    print("********** Check current event ***********")
    for i in tasks:
        token = i.user.token
        username = i.user.name
        for _ in range(len(token.split(SEP))):
            AwaitingDelivery.objects.create(task=i)
        push_message(username, token)
        i.last_request = date.today()
        i.save()
