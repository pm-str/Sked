from django.conf.urls import url
from .views import AwaitingDeliveryAPI

urlpatterns = [
    url(r'awaiting_delivery$', AwaitingDeliveryAPI.as_view(), name='push_token'),
]
