from django.shortcuts import render

from website.models import *

# Create your views here.
def index(request):
    load = Video.objects.filter(name='load')
    context = {
        'load': load,
    }
    return render(request, 'website/index.html', context)

def about(request):
    return render(request, 'website/about.html')
