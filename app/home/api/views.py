from rest_framework.response import Response
from rest_framework.views import APIView
from app.user.models import UserProfile


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
