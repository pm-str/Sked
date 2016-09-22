# coding: utf-8
from django.contrib import messages
from django.utils import timezone
import datetime

class AppContextMixin(object):
    app_header = None

    def get_context_data(self, *args, **kwargs):
        context = super(AppContextMixin, self).get_context_data(**kwargs)
        context['app_header'] = self.app_header
        context['datetime'] = timezone.now()
        a = datetime.date.today()
        context['date'] = "{:%Y-%m-%d}".format(a)
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
