from django.db import models
from django.utils import timezone
import datetime

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

class Organization(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    birth = models.DateField(default=datetime.date.today)
    created_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

class User(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    birth = models.DateField(default=datetime.date.today)
    created_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name



class Team(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    created_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

class UserTeam(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True, blank=True, default='Name')
    description = models.TextField( null=True, blank=True, default='Description')
    birth = models.DateField(default=datetime.date.today)
    created_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
