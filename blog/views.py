from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Movie, MovieHall, Seat, Ticket

def base(request):
    movies = Movie.objects.order_by("?")
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


def movieSchedule(request, movie_id):
	tickets = Ticket.objects.filter()
	movie = Movie.objects.get(id=movie_id)
	arr = MovieHall.objects.filter()
	movie_id = int(movie_id)
	movieHall = []
	for a in arr:
		temp = a.movie.id
		if temp==movie_id:
			movieHall.append(a)
	return render(request,'blog/movieSchedule.html',{'movie':movie, 'movieHall': movieHall, 'tickets':tickets})

def buyTicket(request, ticket_id):
	ticket = Ticket.objects.get(id = ticket_id)
	return render(request,'blog/buyTicket.html',{'ticket':ticket})

def order(request, ticket_id):
	ticket = Ticket.objects.get(id = ticket_id)
	ticket.user = request.user
	ticket.sold = True
	ticket.save()
	return render(request,'blog/order.html',{'ticket':ticket})


