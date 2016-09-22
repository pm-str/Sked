from app.contrib.mixins import AppContextMixin
from django.views.generic import TemplateView
# Create your views here.


class ScheduleView(AppContextMixin, TemplateView):
    template_name = 'schedule/calendar_data.html'
