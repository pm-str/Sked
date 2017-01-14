from django.conf.urls import url

from .views import AddWord, ChangeWord, DeleteWord

urlpatterns = [
    url(r'^dictionary', AddWord.as_view(app_header='Dictionary'), name='dictionary'),
    url(r'^search', "app.english_words.views.search", name='search'),
    url(r'^change_word/(?P<pk>\d+)', ChangeWord.as_view(app_header='Change word'), name='change_word'),
    url(r'^delete_word/(?P<pk>\d+)', DeleteWord.as_view(app_header='Delete word'), name='delete_word'),
]
