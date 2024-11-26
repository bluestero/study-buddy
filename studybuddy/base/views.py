from django.shortcuts import render
from . import models


# Create your views here.

# rooms = [
#     {"id": 1, "name": "Python for beginners."},
#     {"id": 2, "name": "Learn FastAPI with me."},
#     {"id": 3, "name": "Diving in Django together."},
# ]

def home(request):
    rooms = models.Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)

def room(request, pk):
    room = models.Room.objects.get(id = pk)
    context = {"room": room}
    return render(request, "base/room.html", context)
