from rest_framework import serializers
from .models import Film

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = [
            'id',
            'title',
            'description',
            'genre',
            'release_date',
            'director',
            'imdb_rating',
        ]