from rest_framework import serializers


class WordPairSerializer(serializers.Serializer):    
    key_en = serializers.CharField(max_length=256)
    key_jp = serializers.CharField(max_length=256)
