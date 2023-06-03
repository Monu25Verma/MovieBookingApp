from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'theatre_name', 'tickets_allocated']


class MovieSerializerwithoutid(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name', 'theatre_name', 'tickets_allocated']