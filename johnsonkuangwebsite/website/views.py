from django.shortcuts import render

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
    return render(request, 'website/about.html')

def resume(request):
    return render(request, 'website/resume.html')

def blog(request):
    return render(request, 'website/blog.html')

def projects(request):
    return render(request, 'website/projects.html')

def sandbox(request):
    return render(request, 'website/sandbox.html')