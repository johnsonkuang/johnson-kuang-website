from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from website.models import *

# Create your views here.
def index(request):
    load = Video.objects.get(name='load')
    pic = Image.objects.get(caption='About 1 No Blur')
    print(pic.image.height)
    context = {
        'load': load,
        'about': pic,
    }
    return render(request, 'website/index.html', context)

def about(request):
    banner = Image.objects.get(name='about_banner')
    gallery = About_Gallery.objects.all()
    context = {
        'banner': banner,
        'gallery': gallery,
    }
    return render(request, 'website/about.html', context)

def resume(request):
    return render(request, 'website/resume.html')


def projects(request):
    return render(request, 'website/projects.html')

def sandbox(request):
    return render(request, 'website/sandbox.html')