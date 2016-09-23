from django.conf.urls import url
from .views import EventsAPI


urlpatterns = [
    url(r'^get_events', EventsAPI.as_view(), name='api_schedule')
]