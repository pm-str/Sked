from django.conf.urls import url, include
from .views import GetTask, AddEvent

urlpatterns = [
    url(r'^current', GetTask.as_view(app_header='Tasks'), name='current'),
    url(r'^add_event', AddEvent.as_view(app_header='Add event'), name='add_event'),
    url(r'^api/', include('app.home.api.urls'))
    ]


