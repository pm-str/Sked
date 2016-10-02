from django.conf.urls import url, include
from .views import GetTask

urlpatterns = [
    url(r'^current', GetTask.as_view(app_header='Tasks'), name='current'),
    url(r'^api/', include('app.home.api.urls'))
    ]


