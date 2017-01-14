from django.views.generic import TemplateView

from app.contrib.mixins import AppContextMixin


# Create your views here.


class ScheduleView(AppContextMixin, TemplateView):
    template_name = 'schedule/calendar_data.html'
