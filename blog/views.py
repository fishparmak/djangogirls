from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Movie

def base(request):
    movies = Movie.objects.reverse()
    return render(request, 'blog/base.html', {'movies': movies})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})


def movieSchedule(request):
	if request.method == 'GET':
		movie_id = request.GET['movie_id']
		return HttpResponse("Success!") # Sending an success response
	else:
		return HttpResponse("Request method is not a GET")


