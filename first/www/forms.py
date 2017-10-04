from django import forms
from .models import Player, Match, Appearance
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['firstname', 'lastname', 'image']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date', 'cost']

    # This helper creates the Bootstrap settings used by crispy_forms
    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.add_input(Submit('submit', 'Submit'))

class AppearanceForm(forms.ModelForm):
    class Meta:
        model = Appearance
        fields = ['match', 'player', 'paid']
