from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.room.name} - {self.date} ({self.start_time}-{self.end_time})"

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Room, Reservation

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'a.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'b.html', {'room': room})

# urls.py w aplikacji reservations
from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
]

# urls.py w głównym projekcie
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservations.urls')),
]
