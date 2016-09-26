from django.views.generic import TemplateView
from app.contrib.mixins import AppContextMixin
from datetime import datetime, date, time, timedelta
from .models import Task


class GetTask(AppContextMixin, TemplateView):
    template_name = 'home/event_table.html'

    def diff_times(self, start, end):
        diff = (end-start)
        minutes = round((diff.seconds + diff.microseconds / 1000000.0) / 60.0)
        return minutes

    def get_context_data(self, *args, **kwargs):
        table = Task.objects.filter(start_time__day=datetime.today().day).values()
        for i in range(len(table)):
            start = table[i]["start_time"]
            end = table[i]["end_time"]
            table[i]['start_minutes'] = start.hour * 60
            table[i]['length'] = self.diff_times(start, end)
        # print(table)

        kwargs['table'] = table
        kwargs['number_chart'] = self.request.session.get('chart', 0)
        return super(GetTask, self).get_context_data(*args, **kwargs)



