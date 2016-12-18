from app.user.models import UserProfile
from conf.settings import SEP
from rest_framework.response import Response
from rest_framework.views import APIView


class ChartNumAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        try:
            self.request.session['chart'] = self.request.GET.get('number', '0')
        except:
            return Response({}, status=401)
        return Response({}, status=200)


class PushTokenAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):

        try:
            token = self.request.GET['endpoint'].split('/')[-1]
            a = UserProfile.objects.get(user=self.request.user)
            unique_tokens = a.token + SEP + token if a.token else token
            # check to prevent duplications
            a.token = SEP.join(set(unique_tokens.split(SEP)))
            a.save()
        except:
            return Response({}, status=401)
        return Response({}, status=200)


class DelTokenAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        try:
            token = self.request.GET['endpoint'].split('/')[-1]
            a = UserProfile.objects.get(user=self.request.user)
            a.token = SEP.join([i for i in a.token.split(SEP) if i != token])
            a.save()
        except:
            return Response({}, status=401)
        return Response({}, status=200)
