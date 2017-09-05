from django.shortcuts import render
from .models import Player

# Create your views here.
def index(request):
    players = Player.objects.all()
    return render(request, 'index.html', {'players':players})
