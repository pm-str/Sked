from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from app.home.views import redirect_to_home

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^auth/', include('app.loginsys.urls', namespace='auth')),
    url(r'^home/', include('app.home.urls', namespace='home')),
    url(r'^schedule/', include('app.schedule.urls', namespace='schedule')),
    url(r'^english_words/', include('app.english_words.urls', namespace='english_words')),
    url(r'^push_message/', include('app.push_message.urls', namespace='push_message')),
    url(r'^sw(.*.js)$', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),
    url(r'^', redirect_to_home, name='redirect_to_home'),
]