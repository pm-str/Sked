from django.conf.urls import url, include
from django.contrib import admin
from app.home.views import GetTask
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^auth/', include('app.loginsys.urls', namespace='auth')),
    url(r'^home/', include('app.home.urls', namespace='home')),
    url(r'^schedule/', include('app.schedule.urls', namespace='schedule')),
    url(r'^celery/', include('app.celery.urls', namespace='celery')),
    url(r'^push_message/', include('app.push_message.urls', namespace='push_message')),
    url(r'^sw(.*.js)$', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),
    url(r'^$', GetTask.as_view(app_header='Tasks'), name='default'),
]