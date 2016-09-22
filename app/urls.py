from django.conf.urls import url, include
from django.contrib import admin
from app.home.views import GetTask

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('app.loginsys.urls', namespace='auth')),
    url(r'^home/', include('app.home.urls', namespace='home')),
    url(r'^schedule/', include('app.schedule.urls', namespace='schedule')),
    url(r'^', GetTask.as_view(app_header='Tasks'), name='default')
]
