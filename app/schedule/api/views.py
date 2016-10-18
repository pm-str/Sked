from rest_framework.response import Response
from rest_framework.views import APIView
from app.home.models import Task
from app.home.views import get_events_today
from datetime import datetime, date
from calendar import monthrange


class EventsAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):

        today = date.today()
        events_response = []

        for i in range(1, monthrange(today.year, today.month)[1] + 1):
            relative_d = date(today.year, today.month, i)
            query = get_events_today(relative_d, Task)
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

