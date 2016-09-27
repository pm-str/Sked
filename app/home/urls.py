from django.conf.urls import url, include
from .views import GetTask, SetUpPush

urlpatterns = [
    url(r'^current', GetTask.as_view(app_header='Tasks'), name='current'),
    url(r'^push_token', SetUpPush.as_view(app_header='Push'), name='push'),
    url(r'^api/', include('app.home.api.urls'))
    ]


