from django.conf.urls import url
from .views import CheckCurrentMessageAPI


urlpatterns = [
    url(r'check_current_message', CheckCurrentMessageAPI.as_view(), name='CheckCurrentMessage'),
]