from rest_framework.response import Response
from rest_framework import viewsets, status

from . import services
from . import serializers
from . import WordPair


WordPairs = services.getWordPairsFromCsv()


class WordPairViewSet(viewsets.ViewSet):
    serializer_class = serializers.WordPairSerializer

    def list(self, request):
        serializer = serializers.WordPairSerializer(
            instance=WordPairs.values(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            WordPair = WordPairs[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.WordPairSerializer(instance=WordPair)
        return Response(serializer.data)
