from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Cinema, Film, FilmRoom, Place, Ticket, Room

def base(request):
    cinemas = Cinema.objects.filter()
    return render(request, 'ticketapp/base.html', {'cinemas': cinemas})

def cinema(request, cinema_id):
	rooms = Room.objects.filter(cinema=cinema_id)
	cinema = Cinema.objects.get(id=cinema_id)
	return render(request,'ticketapp/cinema.html',{'rooms':rooms, 'cinema': cinema})

def room(request, room_id):
	filmRooms = FilmRoom.objects.filter(room=room_id)
	room = Room.objects.get(id=room_id)
	return render(request,'ticketapp/room.html',{'room':room, 'filmRooms': filmRooms})

def filmRoom(request, filmRoom_id):
	tickets = Ticket.objects.filter(filmRoom=filmRoom_id)
	filmRoom = FilmRoom.objects.get(id=filmRoom_id)
	return render(request,'ticketapp/filmRoom.html',{'filmRoom':filmRoom, 'tickets': tickets})

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
