"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^ticketapp/', include('ticketapp.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ticketapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.base, name='base'),
    url(r'^cinema/(?P<cinema_id>[0-9]+)$', views.cinema, name = 'cinema'),
    url(r'^room/(?P<room_id>[0-9]+)$', views.room, name = 'room'),
    url(r'^filmRoom/(?P<filmRoom_id>[0-9]+)$', views.filmRoom, name = 'filmRoom'),
    url(r'^buyTicket/(?P<ticket_id>[0-9]+)$', views.buyTicket, name = 'buyTicket'),
    url(r'^order/(?P<ticket_id>[0-9]+)$', views.order, name = 'order'),
    url(r'^cabinet/$', views.cabinet, name='cabinet'),
   # url(r'^movieSchedule/(?P<movie_id>\d+)$', views.movieSchedule, name = 'movieSchedule'),
]
