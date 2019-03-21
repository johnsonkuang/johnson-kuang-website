from django import forms
from crispy_forms.helper import FormHelper

from .models import *

class NumPlayersForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = GameInfo
        fields = ['game_name', 'num_players']

        def clean_num_players(self):
            num_players = self.cleaned_data.get('num_players')

            return num_players
        def clean_game_name(self):
            game_name = self.clean_data.get('game_name')
            return game_name

class PlayerCreationForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name', 'hcp']

        #save the data by cleaning it

class HoleForm(forms.ModelForm):

    class Meta:
        model = Holes
        fields = ['']