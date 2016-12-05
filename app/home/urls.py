from django.conf.urls import url, include
from .views import GetTask, AddEvent, ChangeEvent, DeleteEvent

urlpatterns = [
    url(r'^current', GetTask.as_view(app_header='Task & Notice'), name='current'),
    url(r'^search', "app.home.views.search", name='search'),
    url(r'^add_event', AddEvent.as_view(app_header='Add event'), name='add_event'),
    url(r'^change_event/(?P<pk>\d+)', ChangeEvent.as_view(app_header='Change event'), name='change_event'),
    url(r'^delete_event/(?P<pk>\d+)', DeleteEvent.as_view(app_header='Delete event'), name='delete_event'),
    url(r'^api/', include('app.home.api.urls'))
    ]


