from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    theatre_name = models.CharField(max_length=100)
    tickets_allocated = models.IntegerField()