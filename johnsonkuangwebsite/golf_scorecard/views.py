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
from .forms import NumPlayersForm, PlayerCreationForm

# Create your views here.
def initial_form(request):
    form = NumPlayersForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'form': form
    }
    #add html template
    template = ""
    return render(request, template, context)




#needs list, detail, and edit mode
def control_player(request):
    form = PlayerCreationForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        newsletter = Player.objects.get(id=instance.id)

        instance.save()
    context = {
        'form': form,
    }
    # TODO: create template html
    template = 'control_panel/control_newsletter.html'
    return render(request, template, context)

def control_player_list(request):
    players = Player.objects.all()

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
    template = "control_panel/control_newsletter_list.html"
    return render(request, template, context)

def control_player_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)

    context = {
        'player': person,
    }
    # TODO: create template html
    template = 'control_panel/control_newsletter_detail.html'
    return render(request, template, context)

def control_person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        form = PlayerCreationForm(request.POST, instance=person)

        if form.is_valid():
            person = form.save()

            return redirect('control_panel:control_newsletter_detail', pk=person.pk)
    else:
        form = PlayerCreationForm(instance=person)
    context = {
        'form': form,
    }
    template = 'control_panel/control_newsletter.html'
    return render(request, template, context)


def control_player_delete(request, pk):
    player = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        form = PlayerCreationForm(request.POST, instance=player)

        if form.is_valid():
            player.delete()
            return redirect('control_panel:control_newsletter_list')
    else:
        form = PlayerCreationForm(instance=player)

    context = {
        'form':form,
    }

    template = 'control_panel/control_newsletter_delete.html'
    return render(request, template, context)


