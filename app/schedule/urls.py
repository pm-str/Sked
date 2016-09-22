from django.conf.urls import url
from .views import ScheduleView

urlpatterns = [
    url(r'^calendar', ScheduleView.as_view(app_header='Calendar'), name='calendar')
]