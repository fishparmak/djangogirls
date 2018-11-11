from django.shortcuts import render
from django.utils import timezone
from .models import Post

def base(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/base.html', {'posts': posts})

def login(request):
    return render(request, 'blog/login.html')

def home(request):
    return render(request, 'blog/home.html')

def home(request):
    return render(request, 'blog/teams.html')
