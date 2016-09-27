from datetime import date

from app.contrib.mixins import AppContextMixin
from django.views.generic import TemplateView
from .models import Task


class SetUpPush(AppContextMixin, TemplateView):
    template_name = 'base/index.html'


class GetTask(AppContextMixin, TemplateView):
    template_name = 'home/event_table.html'

    def diff_times(self, start, end):
        minutes = end.hour * 60 + end.minute - start.hour * 60 - start.minute
        return minutes

    def get_objects(self):
        today = date.today()
        objects = Task.objects.all()

        answer = objects.filter(repeat='never').filter(date=today)
        answer |= objects.filter(repeat='1day')
        answer |= objects.filter(date__day=today.day)
        answer |= objects.filter(date__month=today.month).filter(date__day=today.day)

        for i in objects.filter(repeat='2day'):
            if (today - i.date).days % 2 == 0:
                answer |= objects.filter(pk=i.pk)
        for i in objects.filter(repeat='1wk'):
            if (today - i.date).days % 7 == 0:
                answer |= objects.filter(pk=i.pk)
        for i in objects.filter(repeat='2wks'):
            if (today - i.date).days % 14 == 0:
                answer |= objects.filter(pk=i.pk)

        return answer

    def get_context_data(self, *args, **kwargs):
        table = self.get_objects().values()
        for i in range(len(table)):
            start = table[i]['start_time']
            end = table[i]['end_time']
            table[i]['start_minutes'] = start.hour * 60
            table[i]['length'] = self.diff_times(start, end)

        kwargs['table'] = table
        kwargs['number_chart'] = self.request.session.get('chart', 0)
        return super(GetTask, self).get_context_data(*args, **kwargs)
