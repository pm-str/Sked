from django.conf.urls import url
from .views import ChartNumAPI, PushTokenAPI, DelTokenAPI


urlpatterns = [
    url(r'chart$', ChartNumAPI.as_view(), name='api'),
    url(r'push_token$', PushTokenAPI.as_view(), name='push_token'),
    url(r'del_token$', DelTokenAPI.as_view(), name='del_token'),
]