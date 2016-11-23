from app.push_message.models import AwaitingDelivery
from rest_framework.response import Response
from rest_framework.views import APIView


class AwaitingDeliveryAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        token = self.request.GET['registration_id']
        try:
            message = AwaitingDelivery.objects.filter(token=token).order_by('datetime').last()
            title = body = None

            if message.task:
                title = message.task.name
                body = message.task.description
            elif message.word:
                title = message.word.name
                body = message.word.description

            message.delete()
            data = {
                'title': title,
                'body': body,
                'icon': 'event.png',
                'url': '/home/current'
                }
            return Response(data, status=200)
        except Exception as r:
            print(r)
            return Response({}, status=401)


