from django.contrib import messages
import os
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from lockdown.decorators import lockdown

from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import NumPlayersForm, PlayerCreationForm, PlayerSelectionForm



# Create your views here.
def init_game(request):
    form = NumPlayersForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        #update the session of the user to include the data inputted
        request.session['num_players'] = instance.num_players
        request.session['game_name'] = instance.game_name

        '''
        template='golf_scorecard/holes.html'
        context= {
            'game_info'
        }
        return render(request, template, )
        '''
        return redirect('golf:player_selection')
    context = {
        'form': form
    }
    #add html template
    template = "golf_scorecard/player_initial.html"
    return render(request, template, context)

def choose_players(request):
    num_players = request.session.get('num_players')
    game_name = request.session.get('game_name')
    form = PlayerSelectionForm(request.POST, num_players=num_players)
    if request.method == 'POST':
        if form.is_valid():
            g = GameInfo.objects.get(game_name=game_name)
            for player in form.cleaned_data.get('players'):
                g.players.add(player)
            return redirect('golf:holes')

    print(form.errors)
    players = Person.objects.all()

    #render a many to many checkbox
    #https://chase-seibert.github.io/blog/2010/05/20/django-manytomanyfield-on-modelform-as-checkbox-widget.html#


    context={
        'players': players,
        'form': form,
        'num_players': num_players,
        'game_name': game_name,
    }
    template = 'golf_scorecard/select_players_form.html'

    return render(request, template, context)

def holes(request):
    num_players = request.session.get('num_players')
    game_name = request.session.get('game_name')
    holes = Holes.objects.all()

    g = GameInfo.objects.get(game_name=game_name)

    context = {
        'holes': holes,
        'game': g,
    }
    template = 'golf_scorecard/scorecard.html'
    return render(request, template, context)


#needs list, detail, and edit mode
def control_player(request):
    form = PlayerCreationForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        person = Person.objects.get(id=instance.id)

        instance.save()
        return redirect('golf:control_players_list')
    context = {
        'form': form,
    }
    # TODO: create template html
    template = 'golf_scorecard/control_player.html'
    return render(request, template, context)

def control_player_list(request):
    players = Person.objects.all()

    paginator = Paginator(players, 10)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index -5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    context = {
        'items': items,
        'page_range': page_range,
    }
    #TODO: create template html
    template = "golf_scorecard/control_player_list.html"
    return render(request, template, context)

def control_player_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)

    context = {
        'player': person,
    }
    # TODO: create template html
    template = 'golf_scorecard/control_player_detail.html'
    return render(request, template, context)

def control_person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        form = PlayerCreationForm(request.POST, instance=person)

        if form.is_valid():
            person = form.save()

            return redirect('golf:control_players_detail', pk=person.pk)
    else:
        form = PlayerCreationForm(instance=person)
    context = {
        'form': form,
    }
    template = 'golf_scorecard/control_player.html'
    return render(request, template, context)


def control_player_delete(request, pk):
    player = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        form = PlayerCreationForm(request.POST, instance=player)

        if form.is_valid():
            player.delete()
            return redirect('golf:control_players_list')
    else:
        form = PlayerCreationForm(instance=player)

    context = {
        'form':form,
    }

    template = 'golf_scorecard/control_player_delete.html'
    return render(request, template, context)


