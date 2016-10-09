from rest_framework.response import Response
from rest_framework.views import APIView
from app.user.models import UserProfile
from ..models import AwaitingDelivery


class ChartNumAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        try:
            self.request.session['chart'] = self.request.GET.get('number', 0)
        except:
            return Response({}, status=401)
        return Response({}, status=200)


class PushTokenAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        try:
            token = self.request.GET['endpoint'].split('/')[-1]
            a = UserProfile.objects.get(user=self.request.user)
            a.token = token
            a.save()
        except:
            return Response({}, status=401)
        return Response({}, status=200)


class DataByRegIdAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        token = self.request.GET['registration_id']
        try:
            first_event = AwaitingDelivery.objects.filter(queue__user__token=token).first()
            data = {
                'title': first_event.queue.name,
                'body': first_event.queue.description,
                'icon': 'event.png',
                'url': '/home/current'
            }
            AwaitingDelivery.objects.filter(queue__user__token=token).first().delete()
            return Response(data, status=200)

        except:
            return Response({}, status=401)


