from django.conf.urls import url
from .views import ChartNumAPI, PushTokenAPI


urlpatterns = [
    url(r'chart$', ChartNumAPI.as_view(), name='api'),
    url(r'push_token$', PushTokenAPI.as_view(), name='push_token'),
]