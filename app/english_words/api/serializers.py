from rest_framework import serializers

from app.english_words.models import Word
from app.user.models import UserProfile


class WordSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=128)
    transcription = serializers.CharField(max_length=128, required=False)
    translation = serializers.CharField(max_length=1000)
    example = serializers.CharField(max_length=1000, required=False)

    def create(self, validated_data):
        """
        Yor should define creating appropriate user

        :param validated_data:
        :return: instance Word object
        """
        validated_data['user'] = UserProfile.objects.get(id=validated_data['id'])
        del (validated_data['id'])
        return Word.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.transcription = validated_data.get('transcription', instance.transcription)
        instance.translation = validated_data.get('translation', instance.translation)
        instance.example = validated_data.get('example', instance.example)
        instance.save()
        return instance
