from rest_framework.response import Response
from rest_framework.views import APIView
from ..tasks import check_current_event


class CheckCurrentEventAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        check_current_event()
        return Response({}, status=200)




