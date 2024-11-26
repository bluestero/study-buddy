from django.shortcuts import render

# Create your views here.

rooms = [
    {"id": 1, "name": "Python for beginners."},
    {"id": 2, "name": "Learn FastAPI with me."},
    {"id": 3, "name": "Diving in Django together."},
]

def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)

def room(request, pk):
    context = {"pk": pk}
    return render(request, "base/room.html", context)
