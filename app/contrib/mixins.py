# coding: utf-8
from django.contrib import messages
from django.utils import timezone
from app.user.models import UserProfile
from app.english_words.models import Settings, Word
from datetime import datetime


class AppContextMixin(object):
    app_header = None

    def current_words(self):
        now = datetime.today()
        try:
            settings = Settings.objects.get(user=UserProfile.objects.get(id=1))
            objects = Word.objects.all()
            quantity = (now - datetime.combine(now.date(), settings.start_time)).seconds // (settings.range * 60)
            ind1 = settings.number_word - min(settings.number_word, quantity)
            ind2 = settings.number_word
            query = objects[ind1:ind2]
            return query
        except Exception as r:
            print(r)
            return ''

    def get_context_data(self, *args, **kwargs):
        context = super(AppContextMixin, self).get_context_data(**kwargs)
        context['app_header'] = self.app_header
        context['datetime'] = timezone.now()
        a = datetime.today().date()
        context['date'] = "{:%Y-%m-%d}".format(a)
        context['current_words'] = self.current_words()
        return context

    def __init__(self, *args, **kwargs):
        self.app_header = kwargs['app_header']
        super(AppContextMixin, self).__init__(*args, **kwargs)


class MessageMixin(object):
    """
    Make it easy to display notification messages when using Class Based Views.
    """

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)
