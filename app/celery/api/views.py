from app.english_words.tasks import check_current_word
from app.home.tasks import check_current_event
from app.push_message.functions import clear_queue
from rest_framework.response import Response
from rest_framework.views import APIView


class CheckCurrentMessageAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        check_current_event()
        check_current_word()
        clear_queue()
        return Response({'Success'}, status=200)
