from django import forms
from .models import Player, Match, Appearance

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['firstname', 'lastname', 'image']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date', 'cost']

class AppearanceForm(forms.ModelForm):
    class Meta:
        model = Appearance
        fields = ['match', 'player', 'paid']
