from django.http import JsonResponse
from .models import Movie
from django.core import serializers

# Create your views here.
class MovieView:
    def all(request):
        movies = Movie.objects.all()
        data = serializers.serialize('json', movies) #deserialize
        return JsonResponse(data, safe=False) #serialize
    
    def search_movie(request,**kwargs):
        movies = Movie.objects.get(movie_name = kwargs.get('moviename'))
        data = serializers.serialize('json', movies) #deserialize
        return JsonResponse(movies, safe=False) #serialize