from django.http import JsonResponse
from .models import Movies, Tickets
from rest_framework import viewsets
from rest_framework.decorators import action
import logging as logger
from django.shortcuts import get_object_or_404
from .serializer import MovieSerializer,MovieSerializerwithoutid, MovieSerializeridname,TicketSerializer

# Create your views here.
class MovieView(viewsets.ModelViewSet):

    @action(detail=False, methods=['get'])
    def all(self,request):
        movies = Movies.objects.all()
        movie_serialized = MovieSerializer(movies,many = True)  #deserialize
        return JsonResponse(movie_serialized.data, safe=False) #serialize
    
    @action(detail=False, methods=['get'])
    def search_movie_containing(self,request,**kwargs):
        movies = Movies.objects.filter(movie_name__icontains =str(kwargs['moviename'])) # user -> db
        movie_serialized = MovieSerializer(movies,many = True) #db -> python   deserialize
        # for movie in movie_serialized.data:
        #     print((movie['id']*4)**3)
        # # (id * 4)^3
        return JsonResponse(movie_serialized.data, safe=False) #serialize
    
    # @action(detail=False, methods=['get'])
    # def search_particular_movie(self,request,**kwargs):
    #     movies = Movie.objects.filter(movie_name =str(kwargs['moviename']))
    #     movie_serialized = MovieSerializerwithoutid(movies,many = True)
    #     return JsonResponse(movie_serialized.data, safe=False) #serialize
    
    # @action(detail=False, methods=['get'])
    # def search_with_theatername_movie(self,request,**kwargs):
    #     movies = Movie.objects.filter(theatre_name__contains =str(kwargs['theatre_name']))  #database call
    #     movie_serialized = MovieSerializeridname(movies,many = True) #deserialize
    #     for movie in movie_serialized.data:
    #         movie['movie_name'] = str(movie['movie_name']).upper()
    #     return JsonResponse(movie_serialized.data, safe=False) #serialize


class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    @action(detail=False, methods=['post'])
    def add_ticket(self,request, **kwargs):
        try:
            movie = Movies.objects.get(movie_name = str(kwargs['moviename']))
    
            no_ticket = request.data.get('no_of_tickets')
            seat_no = request.data.get('seat_number')
            if int(no_ticket) <= movie.seats_allocated:
                ticket = Tickets(movie_id = movie, no_of_tickets = no_ticket,seat_number = seat_no)
                ticket.save()

                Movie_Serializer= MovieSerializer(movie)
                Ticket_Serializer = TicketSerializer(ticket)
                response_data ={ 
                    'movie':Movie_Serializer.data,
                    'ticket':  Ticket_Serializer.data
                }
                logger.info('ticket has booked')
                return JsonResponse(response_data)
            else:
                return JsonResponse({'message':"not enough ticket available"}, status = 400)
        except Movies.DoesNotExist:
            logger.error('movie does not exists')
            return JsonResponse({'message':"movie does not exists"}, status = 404)

    def list(self, request): 
        tickets =  Tickets.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return JsonResponse(serializer.data, safe=False)

class MovieViewSetAdmin(viewsets.ViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=['put'])
    def update_ticket_seat_avl(self,request,movie_name=None,movie_id=None):
        
        movie = get_object_or_404(Movies, id = movie_id)
        movie_id = movie_id
        movie_name = movie.movie_name
        tickets = Tickets.objects.filter(movie=movie_id)

        total_ticket_booked = tickets.aggregate(total = sum('no_of_tickets'))['total']
        total_ticket_booked = total_ticket_booked if total_ticket_booked else 0

        seat_available = movie.seats_allocated - total_ticket_booked
        seat_available = seat_available if seat_available >= 0 else 0


        if seat_available == 0:
            status = 'SOLD OUT'
        else:
            status = 'book  ASAP'
            logger.info('Tickets Status: %s', status)

            movie.seats_allocated = seat_available
            movie.save()
            logger.info('Movie updated!')
            response_data = {
            'message': f'Successfully updated seats available for movie "{movie_name}"',
            'seat_available': seat_available,
            'ticket_status': status
        }
        return JsonResponse(response_data)






    

