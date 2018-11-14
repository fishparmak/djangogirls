from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Film, FilmRoom, Place, Ticket

def base(request):
    movies = Film.objects.order_by("?")
    return render(request, 'ticketapp/base.html', {'movies': movies})

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
    return render(request, 'ticketapp/signup.html', {'form': form})


def movieSchedule(request, movie_id):
	tickets = Ticket.objects.filter()
	movie = Film.objects.get(id=movie_id)
	arr = FilmRoom.objects.filter()
	movie_id = int(movie_id)
	movieRoom = []
	for a in arr:
		temp = a.movie.id
		if temp==movie_id:
			movieRoom.append(a)
	return render(request,'ticketapp/movieSchedule.html',{'movie':movie, 'movieRoom': movieRoom, 'tickets':tickets})

def buyTicket(request, ticket_id):
	ticket = Ticket.objects.get(id = ticket_id)
	return render(request,'ticketapp/buyTicket.html',{'ticket':ticket})

def order(request, ticket_id):
	ticket = Ticket.objects.get(id = ticket_id)
	ticket.user = request.user
	ticket.sold = True
	ticket.save()
	return render(request,'ticketapp/order.html',{'ticket':ticket})

def cabinet(request):
	tickets = Ticket.objects.filter(user = request.user)
	return render(request,'ticketapp/cabinet.html',{'tickets':tickets})
