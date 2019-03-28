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


class PlayerSelectionForm(forms.Form):
    players = forms.ModelMultipleChoiceField(label='Select Players',
                                             widget=forms.SelectMultiple,
                                             queryset=Person.objects.all())

    num_players = 0
    def set_globalvar_to_number(self, num):
        global num_players
        num_players = num

    def __init__(self, *args, **kwargs):
        num_players = kwargs.pop('num_players')
        super(PlayerSelectionForm, self).__init__(*args, **kwargs)
        self.set_globalvar_to_number(num=num_players)

    def clean_players(self):
        print('nope')
        value = self.cleaned_data['players']
        if len(value) > num_players:
            raise forms.ValidationError("You can't select more than " + num_players + " players.")
        return value
