from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import word_detail, word_list

urlpatterns = [
    url(r'^word_detail/(?P<name>[\w]+)$', word_detail),
    url(r'^word_list$', word_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
