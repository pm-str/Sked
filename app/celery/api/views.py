from rest_framework.response import Response
from rest_framework.views import APIView
from app.home.tasks import check_current_event
from app.english_words.tasks import check_current_word


class CheckCurrentMessageAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        check_current_event()
        check_current_word()
        return Response({}, status=200)




