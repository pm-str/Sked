from django.shortcuts import render_to_response, redirect
from django.views.generic import TemplateView
from app.contrib.mixins import AppContextMixin
from .models import Task


class GetTask(AppContextMixin, TemplateView):
    template_name = 'home/event_table.html'

    def get_context_data(self, *args, **kwargs):
        kwargs['table'] = Task.objects.all()
        kwargs['number_chart'] = self.request.session['chart']
        return super(GetTask, self).get_context_data(*args, **kwargs)


def change_chart(request, number):
    request.session['chart'] = number
    return redirect('home:current')
