from datetime import datetime, timedelta

from app.push_message.models import AwaitingDelivery
from conf.settings import GCM_APIKEY
from gcm import GCM

TIME_TO_LIVE = 86400


def push_message(username, token, pk):
    gcm = GCM(GCM_APIKEY)
    try:
        gcm.plaintext_request(registration_id=token, data={}, collapse_key='new', time_to_live=TIME_TO_LIVE)
    except Exception as r:
        # delete task from queue
        AwaitingDelivery.objects.filter(pk=pk)[0].delete()
        print('Exception was occurred: ', r)
    else:
        print('Message was sent to {}'.format(username.encode('utf-8')))


def clear_queue():
    AwaitingDelivery.objects.all().delete()

