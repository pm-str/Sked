from rest_framework.response import Response
from rest_framework.views import APIView
from app.home.models import Task


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
                'start': event.start_time.isoformat()[:19],
                'end': event.end_time.isoformat()[:19]
            })
        return Response(events_response)

