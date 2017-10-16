from django.shortcuts import render, redirect
from .models import Player, Match
from .forms import PlayerForm, MatchForm
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.http import HttpResponse

# Create your views here.
def index(request):
    players = Player.objects.all()
    return render(request, 'index.html', {'players':players})

def matches(request):
    if request.user.is_authenticated():
        matches = Match.objects.all()
        return render(request, 'matches.html', {'matches':matches})
    else:
        return render(request, 'unauthenticated.html')

def matches_edit(request, match_id):
    match = Match.objects.get(pk=match_id)
    if (request.method == 'POST'):
        # Process the form
        form = MatchForm(data=request.POST, instance=match)
        if form.is_valid():
            form.save(commit = True)
        return redirect(reverse('matches'))
    else:
        match_dict = model_to_dict(match)
        form = MatchForm(match_dict)
        top_ten_players = Player.objects.all()[:10]
        remaining_players = Player.objects.all()[10:]
        return render(request, 'matches_edit.html', {'form':form,
            'top_ten_players':top_ten_players,
            'remaining_players':remaining_players})

def matches_new(request):
    if (request.method == 'POST'):
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect(reverse('matches'))
    else:
        form = MatchForm()
        top_ten_players = Player.objects.all()[:10]
        remaining_players = Player.objects.all()[10:]
    return render(request, 'matches_edit.html', {'form':form,
        'top_ten_players':top_ten_players,
        'remaining_players':remaining_players})

def players(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players':players})

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

def verify_email(backend, user, response, *args, **kwargs):
    # if backend.name == "google-oauth2":
        # user.is_authenticated = True
        # user.save()

    username = kwargs.get('details').get('fullname')
