from django.conf.urls import url
from .views import GetTask

urlpatterns = [
    url(r'^current', GetTask.as_view(app_header='Tasks'), name='current'),
    url(r'^chart(?P<number>\d+)', 'app.home.views.change_chart', name='set_chart')
    ]


