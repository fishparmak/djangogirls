from django.contrib import admin
from .models import Post, Cinema, MovieHall, Ticket, Hall, Seat, Movie

admin.site.register(Post)
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Ticket)
admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(MovieHall)
