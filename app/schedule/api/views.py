from calendar import monthrange
from datetime import datetime, date

from app.home.models import Task
from app.home.views import get_events_today
from rest_framework.response import Response
from rest_framework.views import APIView


class EventsAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):

        today = date.today()
        events_response = []

        for month in range(max(today.month - 1, 1), min(today.month + 1, 12) + 1):
            for day in range(1, monthrange(today.year, month)[1] + 1):
                relative_d = date(today.year, month, day)
                query = get_events_today(relative_d, Task.objects.all())
                for event in query:
                    events_response.append({
                        'title': event.name,
                        'start': datetime.combine(relative_d, event.start).isoformat()[:19],
                        'end': datetime.combine(relative_d, event.end).isoformat()[:19],

                        # it does not work for some reason
                        'color': 'brawn',
                        'textColor': 'white'
                    })
        return Response(events_response)

