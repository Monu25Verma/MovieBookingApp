from rest_framework import serializers
from .models import Movies
from .models import Tickets

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'movie_name', 'theatre_name', 'seats_allocated']

class MovieSerializerwithoutid(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['movie_name', 'theatre_name', 'seats_allocated']

class MovieSerializeridname(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id','movie_name']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ['movie_id','no_of_tickets', 'seat_number']