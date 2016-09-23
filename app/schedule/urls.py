from django.conf.urls import url, include
from .views import ScheduleView

urlpatterns = [
    url(r'^calendar', ScheduleView.as_view(app_header='Calendar'), name='calendar'),
    url(r'^api/', include('app.schedule.api.urls'))
]