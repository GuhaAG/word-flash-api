from rest_framework import serializers


class WordPairSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    key_en = serializers.CharField(max_length=256)
    key_jp = serializers.CharField(max_length=256)
