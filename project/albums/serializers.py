from rest_framework.serializers import ModelSerializer
from .models import Albums, Musician


class MusicianSerializer(ModelSerializer):

    class Meta:
        model = Musician
        fields = '__all__'


class AlbumSerializer(ModelSerializer):

    class Meta:
        model = Albums
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['artist'] = MusicianSerializer(instance.artist).data
        return data