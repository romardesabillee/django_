from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Albums
from .serializers import AlbumSerializer

class AlbumView(ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'id'

    # def list(self, request, *args, **kwargs):
    #     album = Albums.objects.first()
    #     all_albums = Albums.objects.all().values()

    #     return Response(all_albums)