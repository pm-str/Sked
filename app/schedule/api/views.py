from rest_framework.response import Response
from rest_framework.views import APIView
from app.home.models import Task
from datetime import datetime


class EventsAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        try:
            events = Task.objects.all()
        except:
            return Response({
                'result': 'error',
                'code': 1
            })
        events_response = []
        for event in events:
            events_response.append({
                'title': event.name,
                'start': datetime.combine(event.date, event.start).isoformat()[:19],
                'end': datetime.combine(event.date, event.end).isoformat()[:19],

                # it does not work for some reason
                'color': 'brawn',
                'textColor': 'white'
            })
        return Response(events_response)

