from gcm import GCM
from conf.settings import GCM_APIKEY


def push_message(username, token):
    gcm = GCM(GCM_APIKEY)
    gcm.plaintext_request(registration_id=token, data={})
    print(" ***** The message was sent to {}\ntoken - {} ***** ".format(username, token))