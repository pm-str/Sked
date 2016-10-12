from datetime import date, datetime

from app.contrib.mixins import AppContextMixin
from django.views.generic import TemplateView
from .models import Task


class AddEvent(AppContextMixin, TemplateView):
    pass


def get_events_today(events):
    today = date.today()
    objects = events.objects.all()

    answer = objects.filter(repeat='never').filter(date=today)
    answer |= objects.filter(repeat='1day')

    for i in objects.filter(repeat='2day'):
        if (today - i.date).days % 2 == 0:
            answer |= objects.filter(pk=i.pk)
    for i in objects.filter(repeat='1wk'):
        if (today - i.date).days % 7 == 0:
            answer |= objects.filter(pk=i.pk)
    for i in objects.filter(repeat='2wks'):
        if (today - i.date).days % 14 == 0:
            answer |= objects.filter(pk=i.pk)
    answer |= objects.filter(repeat='mn').filter(date__day=today.day)
    answer |= objects.filter(repeat='yr').filter(date__month=today.month).filter(date__day=today.day)

    return answer.order_by('time_notice')


class GetTask(AppContextMixin, TemplateView):
    template_name = 'home/event_table.html'

    def diff_times(self, start, end):
        minutes = end.hour * 60 + end.minute - start.hour * 60 - start.minute
        return minutes

    def get_context_data(self, *args, **kwargs):
        table = get_events_today(Task).values()
        for i in range(len(table)):
            start = table[i]['start']
            end = table[i]['end']
            table[i]['length'] = self.diff_times(start, end)
            # For range chart
            table[i]['start_minutes'] = start.hour * 60 + start.minute
            table[i]['time_now'] = datetime.today().time()

        kwargs['table'] = table
        kwargs['number_chart'] = self.request.session.get('chart', 0)
        return super(GetTask, self).get_context_data(*args, **kwargs)
