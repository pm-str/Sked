from django.conf.urls import url
from .views import ChartNumAPI, PushTokenAPI, DataByRegIdAPI


urlpatterns = [
    url(r'chart$', ChartNumAPI.as_view(), name='api'),
    url(r'push_token$', PushTokenAPI.as_view(), name='push_token'),
    url(r'data_by_reg_id$', DataByRegIdAPI.as_view(), name='push_token'),

]