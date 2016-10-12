from .models import Settings, Word
from app.push_message.send import push_message
from app.push_message.models import AwaitingDelivery
from datetime import datetime
from celery import shared_task


# converting to the datetime format
# thus we will able to subtract times
def dt(time):
    return datetime.combine(datetime.today().date(), time)


@shared_task()
def check_current_word():
    print("********** Check current word ***********")

    objects = Settings.objects.all()
    for i in objects:
        now = datetime.today()
        username = i.user.name
        token = i.user.token
        if ((now - dt(i.last_request)).seconds > i.range * 60) and dt(i.start_time) <= now <= dt(i.end_time):
            i.last_request = now.time()
            i.number_word += 1
            i.save()
            number_word = min(Word.objects.count(), i.number_word)
            AwaitingDelivery.objects.create(word=Word.objects.all()[number_word])
            push_message(username, token)


