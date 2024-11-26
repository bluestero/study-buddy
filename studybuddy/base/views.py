from django.shortcuts import render
from . import models, forms


# Create your views here.
def home(request):
    rooms = models.Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)

def room(request, pk):
    room = models.Room.objects.get(id = pk)
    context = {"room": room}
    return render(request, "base/room.html", context)

def create_room(request):
    form = forms.RoomForm()
    context = {"form": form}
    return render(request, "base/room_form.html", context)
