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
        return self.title        return self.title

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Cinema(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Hall(models.Model):
    name = models.CharField(max_length=200)
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Seat(models.Model):
    sold = models.BooleanField()
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    def __str__(self):
        return self.id