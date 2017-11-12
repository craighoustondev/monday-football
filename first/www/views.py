from django.shortcuts import render, redirect
from .models import Appearance, Match, Player
from .forms import PlayerForm, MatchForm
from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.http import HttpResponse
from django.db.models import Q

import json

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

        included_players = Player.objects.filter(appearance__match__id=match_id)
        excluded_players = Player.objects.exclude(pk__in=included_players)

        return render(request, 'matches_edit.html', {
            'form':form,
            'included_players':included_players,
            'excluded_players':excluded_players
            })

def matches_new(request):
    if (request.method == 'POST'):
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/')
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

def submit_appearances(request):
    if (request.method == 'POST'):
        player_ids_from_request = request.POST.getlist('playerIds[]')
        player_ids = [int(p) for p in player_ids_from_request]
        match_id = request.POST.get('matchId')

        current_player_ids = list(Appearance.objects.filter(
            match__id=match_id).values_list('player', flat=True))

        # Delete any existing player appearances that are no longer included
        players_for_delete = [p for p in current_player_ids if p not in player_ids]

        for player in players_for_delete:
            appearance_for_delete = Appearance.objects.get(
                match__id=match_id, player=player)
            appearance_for_delete.delete()

        for player_id in player_ids:
            match = Match.objects.get(pk=match_id)
            player = Player.objects.get(pk=player_id)
            appearance = Appearance(match=match, player=player, paid=True)
            try:
                appearance.save()
            except IntegrityError as e:
                print(e)
                continue

        return HttpResponse(
            json.dumps({"result": "Create appearance successful!"}),
            content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json")

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

def verify_email(backend, user, response, *args, **kwargs):
    # if backend.name == "google-oauth2":
        # user.is_authenticated = True
        # user.save()

    username = kwargs.get('details').get('fullname')
