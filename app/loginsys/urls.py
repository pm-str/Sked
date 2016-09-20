# coding: utf-8
from django.conf.urls import url

urlpatterns = [
    url(r'^login$', 'app.loginsys.views.login', name='login'),
    url(r'^logout$', 'app.loginsys.views.logout', name='logout')
]
