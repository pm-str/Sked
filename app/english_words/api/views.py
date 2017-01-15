from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from app.english_words.api.serializers import WordSerializer
from app.english_words.models import Word


@api_view(['GET', 'POST'])
def word_list(request, format=None):
    if request.method == 'GET':
        snippets = Word.objects.all()
        serializer = WordSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # the entered field value doesn't matter
        data['id'] = request.user.id
        serializer = WordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def word_detail(request, name, format=None):
    try:
        word = Word.objects.get(name=name)
    except Word.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        # the entered field value doesn't matter
        data['id'] = request.user.id
        data['name'] = data.get('name', word.name)
        data['translation'] = data.get('translation', word.translation)
        serializer = WordSerializer(word, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        word.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
