from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=100) 
    theatre_name = models.CharField(max_length=100)
    seats_allocated = models.IntegerField()


class Tickets(models.Model):
    movie_id  = models.ForeignKey(Movies, on_delete=models.CASCADE)
    no_of_tickets = models.IntegerField()
    seat_number = models.CharField()

    