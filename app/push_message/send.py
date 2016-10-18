from gcm import GCM
from conf.settings import GCM_APIKEY, SEP
from app.push_message.models import AwaitingDelivery


def push_message(username, token):
    gcm = GCM(GCM_APIKEY)
    for i in token.split(SEP):
        try:
            gcm.plaintext_request(registration_id=i, data={})
        except Exception as r:
            # delete task from queue
            task_object = AwaitingDelivery.objects.filter(task__user__token__contains=token)
            word_object = AwaitingDelivery.objects.filter(word__user__token__contains=token)
            if task_object.count():
                task_object.first().delete()
            elif word_object.count():
                word_object.first().delete()
            print('Exception was occurred: ', r)
        else:
            print('Message was sent to {}\ntoken - {}'.format(username, i))
