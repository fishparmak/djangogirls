from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200, default='Film')
    info = models.TextField(default='Film Info...')
    def __str__(self):
        return self.title

class Cinema(models.Model):
    title = models.CharField(max_length=200, default='Cinema')
    info = models.TextField(default='Cinema Info...')
    def __str__(self):
        return self.title

class Room(models.Model):
    title = models.CharField(max_length=200, default='Room')
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Place(models.Model):
    number = models.IntegerField(default=1)
    def __str__(self):
        return str(self.number)

class Ticket(models.Model):
    price = models.DecimalField(default=2, decimal_places = 1, max_digits = 5)
    booked = models.BooleanField(default='False')
    filmRoom = models.ForeignKey('FilmRoom', on_delete=models.CASCADE)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True, default='user')
    def __str__(self):
        return str(self.place)

class PlaceRoom(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.room) + str('-') + str(self.place))

class FilmRoom(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    film = models.ForeignKey('Film', on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return (str(self.film) + str(' in ') + str(self.room))
