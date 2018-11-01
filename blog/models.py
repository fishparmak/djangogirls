from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title





class Movie(models.Model):
    name = models.CharField(max_length=200, default='Movie')
    description = models.TextField(default='This is Movie description')

    def __str__(self):
        return self.name

class Cinema(models.Model):
    name = models.CharField(max_length=200, default='Cinema')
    description = models.TextField(default='This is Cinema description')
    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=200, default='Hall')
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Seat(models.Model):
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class MovieHall(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name

class Ticket(models.Model):
    sold = models.BooleanField(default='False')
    cost = models.DecimalField(default=5.99, max_digits = 6, decimal_places = 2)
    movieHall = models.ForeignKey('MovieHall', on_delete=models.CASCADE)
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.seat

