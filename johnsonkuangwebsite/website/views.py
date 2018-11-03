from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from website.models import *

# Create your views here.
def index(request):
    load = Video.objects.get(name='load')
    load_image = Image.objects.get(name='home_load_graphic')
    about = Image.objects.get(name='about_parallax')
    blog = Image.objects.get(name='blog_parallax')

    context = {
        'load_pic': load_image,
        'load': load,
        'about': about,
        'blog': blog,
    }
    return render(request, 'website/index.html', context)

def about(request):
    #banner = Image.objects.get(name='about_banner')
    gallery = About_Gallery.objects.all()
    context = {
     #   'banner': banner,
        'gallery': gallery,
    }
    return render(request, 'website/about.html', context)

#helper function to pack the list into two per row
def pack(_list):
    new_list = list(zip(_list[::2], _list[1::2]))
    if len(_list) % 2:
        new_list.append((_list.last(), None))
    return new_list

def resume(request):
    banner = Image.objects.get(name='seattle_background')
    headshot = Image.objects.get(name='resume_headshot')
    experiences = ResumeWorkExperience.objects.all()
    skills = ResumeSkill.objects.all()
    skills = pack(skills)
    education = ResumeEntryEducation.objects.all()
    about = ResumeEntryBasicInfo.objects.all()[0]
    phone_number = "%s%s%s-%s%s%s-%s%s%s%s" % tuple(str(about.phone))
    context = {
        'banner': banner,
        'headshot': headshot,
        'experiences': experiences,
        'skills': skills,
        'education': education,
        'about': about,
        'phone': phone_number,
    }
    return render(request, 'website/resume.html', context)


def projects(request):
    return render(request, 'website/projects.html')

def sandbox(request):
    return render(request, 'website/sandbox.html')

def terms(request):
    return render(request, 'website/termsofuse.html')