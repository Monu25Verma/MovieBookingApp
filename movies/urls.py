from django.urls import path
from .views import MovieView,TicketView, MovieViewSetAdmin,GraphView   #Graph3DView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies', MovieView,basename='movie'),
router.register(r'tickets', TicketView,basename='movie')

urlpatterns = [
    path('all/',MovieView.as_view({'get':'all'}),name ='all'),
    path('movies/<str:moviename>',MovieView.as_view({'get':'search_movie_containing'}), name ='search_movie_containing'),
    # path('movie/<str:moviename>',MovieView.as_view({'get':'search_particular_movie'}), name ='search_movie_particular'),
    # path('movie/<int:id>/',MovieView.as_view({'get':'search_particularid_movie'}), name ='search_movie_particularid'),
    # path('theater/<str:theatre_name>',MovieView.as_view({'get':'search_with_theatername_movie'}), name ='search_movie_particulartheater'),
    path('<str:moviename>/add/',TicketView.as_view({'post':'add_ticket'}), name ='add_ticket'),
    path('<str:movie_name>/update/<int:movie_id>/',MovieViewSetAdmin.as_view({'put':'update_ticket_seat_avl'}), name ='update_ticket'),
    path('graph/', GraphView.as_view({'get':'all_movies_with_tickets'}), name='all_movies_with_tickets'),
    #path('graph/', Graph3DView.as_view({'get':'all_movies_with_tickets'}), name='all_movies_with_tickets'),
]
