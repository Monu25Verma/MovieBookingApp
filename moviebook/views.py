from django.http import JsonResponse
from .models import Movie
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializer import MovieSerializer,MovieSerializerwithoutid, MovieSerializeridname

# Create your views here.
class MovieView(viewsets.ModelViewSet):

    @action(detail=False, methods=['get'])
    def all(self,request):
        movies = Movie.objects.all()
        movie_serialized = MovieSerializer(movies,many = True)
        return JsonResponse(movie_serialized.data, safe=False) #serialize
    
    @action(detail=False, methods=['get'])
    def search_movie_containing(self,request,**kwargs):
        movies = Movie.objects.filter(movie_name__contains =str(kwargs['moviename']))
        movie_serialized = MovieSerializer(movies,many = True)
        return JsonResponse(movie_serialized.data, safe=False) #serialize
    

    @action(detail=False, methods=['get'])
    def search_particular_movie(self,request,**kwargs):
        movies = Movie.objects.filter(movie_name =str(kwargs['moviename']))
        movie_serialized = MovieSerializerwithoutid(movies,many = True)
        return JsonResponse(movie_serialized.data, safe=False) #serialize
    
    @action(detail=False, methods=['get'])
    def search_with_theatername_movie(self,request,**kwargs):
        movies = Movie.objects.filter(theatre_name__contains =str(kwargs['theatre_name']))  #database call
        movie_serialized = MovieSerializeridname(movies,many = True) #deserialize
        return JsonResponse(movie_serialized.data, safe=False) #serialize