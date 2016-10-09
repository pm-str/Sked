from django.conf.urls import url
from .views import CheckCurrentEventAPI


urlpatterns = [
    url(r'check_current_event', CheckCurrentEventAPI.as_view(), name='CheckCurrentEvent'),
]