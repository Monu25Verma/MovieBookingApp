from django.urls import path
from .views import MovieView

urlpatterns = [
    path('all/',MovieView.all, name ='all'),
    path('movies/<str:moviename>',MovieView.search_movie, name ='search_movie')
]