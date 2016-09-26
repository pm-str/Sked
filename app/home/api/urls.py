from django.conf.urls import url
from .views import ChartNumAPI


urlpatterns = [
    url(r'chart$', ChartNumAPI.as_view(), name='api')
]