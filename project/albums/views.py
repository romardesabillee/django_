from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import (
    Albums,
    Musician
)
from .serializers import (
    AlbumSerializer,
    MusicianSerializer
)


class AlbumView(ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'id'

    # def list(self, request, *args, **kwargs):
    #     album = Albums.objects.first()
    #     all_albums = Albums.objects.all().values()

    #     return Response(all_albums)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=204)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


class MusicianView(ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    lookup_field = 'id'