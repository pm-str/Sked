from datetime import datetime

from app.push_message.functions import push_message
from app.push_message.models import AwaitingDelivery
from conf.settings import SEP


def check_current_word():
    from .models import Settings, Word
    print("********** Check current word ***********")
    dt = lambda x: datetime.combine(datetime.today().date(), x)

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
            word = Word.objects.all().order_by('id')[number_word]
            word.last_request = now
            word.save()
            for one_token in token.split(SEP):
                a = AwaitingDelivery.objects.create(word=word, token=one_token)
                push_message(username, one_token, a.pk)
