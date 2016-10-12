from rest_framework.response import Response
from rest_framework.views import APIView
from app.push_message.models import AwaitingDelivery


class AwaitingDeliveryAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        token = self.request.GET['registration_id']
        try:
            task_object = AwaitingDelivery.objects.filter(task__user__token=token)
            word_object = AwaitingDelivery.objects.filter(word__user__token=token)
            title = body = None
            if task_object.count():
                title = task_object.first().task.name
                body = task_object.first().task.description
                task_object.first().delete()
            elif word_object.count():
                title = word_object.first().word.name
                body = word_object.first().word.description
                word_object.first().delete()
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


