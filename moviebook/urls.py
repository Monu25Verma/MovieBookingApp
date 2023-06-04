from django.urls import path
from .views import MovieView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies', MovieView,basename='movie')

urlpatterns = [
    path('all/',MovieView.as_view({'get':'all'}),name ='all'),
    path('movies/<str:moviename>',MovieView.as_view({'get':'search_movie_containing'}), name ='search_movie_containing'),
    path('movie/<str:moviename>',MovieView.as_view({'get':'search_particular_movie'}), name ='search_movie_particular'),
    path('movie/<int:id>/',MovieView.as_view({'get':'search_particularid_movie'}), name ='search_movie_particularid'),
    path('theater/<str:theatre_name>',MovieView.as_view({'get':'search_with_theatername_movie'}), name ='search_movie_particulartheater'),

]
