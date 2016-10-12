from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('app.push_message.api.urls'))
]