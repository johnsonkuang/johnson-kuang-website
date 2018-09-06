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

def resume(request):
    return render(request, 'website/resume.html')

def blog(request):
    return render(request, 'website/blog.html')

def projects(request):
    return render(request, 'website/projects.html')

def sandbox(request):
    return render(request, 'website/sandbox.html')