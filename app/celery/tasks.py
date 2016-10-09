from gcm import GCM
from datetime import datetime, date
from app.home.models import Task, AwaitingDelivery
from celery import shared_task


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


def push_all():
    print("####################3")
    for i in Task.objects.all():
        token = i.user.token
        username = i.user.name
        push_task(username, token)


def push_task(username, token):
    gcm = GCM("AIzaSyCNREuhmag35fb3Rn6e9C1rAJ6rU22yPLg")
    gcm.plaintext_request(registration_id=token, data={})
    print(" ***** The message was sent to {}\ntoken - {} ***** ".format(username, token))


@shared_task()
def check_current_event():
    tasks = get_notice_today(Task)
    print("********** It works ***********")
    for i in tasks:
        token = i.user.token
        username = i.user.name
        temp = AwaitingDelivery.objects.create(queue=i)
        temp.save()
        push_task(username, token)
        i.last_request = date.today()
        i.save()
