from django.contrib import messages
import os
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from lockdown.decorators import lockdown

from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

from website.models import *
from .forms import NewsletterUserSignUpForm, NewsletterCreationForm

# Create your views here.
def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request,
                             'Your email already exists in our database',
                             "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request,
                             'Your email has been submitted to the database',
                             "alert alert-success alert-dismissible")
            subject = "Thank You For Joining My Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(os.path.join(settings.BASE_DIR,'website', 'templates','website','sign_up_email.txt')) as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template('website/sign_up_email.html').render()
            message.attach_alternative(html_template, "text/html")
            message.send()


    context = {
        'form': form
    }
    template = "website/sign_up.html"
    return render(request, template, context)

def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request,
                             'Your email has been removed, please consider contacting me with your complaints and resubscribing',
                             'alert alert-success alert-dismissible')
            subject = "You have been unsubscribed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(os.path.join(settings.BASE_DIR,'website', 'templates','website','unsubscribe_email.txt')) as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template('website/unsubscribe_email.html').render()
            message.attach_alternative(html_template, "text/html")
            message.send()
        else:
            messages.warning(request,
                             'Your email is not in the database',
                             'alert alert-warning alert-dismissible')

    context = {
        'form': form,
    }
    template = 'website/unsubscribe.html'
    return render(request, template, context)

def control_newsletter(request):
    form = NewsletterCreationForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        newsletter = Newsletter.objects.get(id=instance.id)
        if newsletter.status == 'Published':
            subject = newsletter.subject
            body = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            for email in newsletter.email.all():
                send_mail(subject=subject, from_email=from_email, recipient_list=[email],message=body, fail_silently=True)
        instance.save()
    context = {
        'form': form,
    }
    template = 'control_panel/control_newsletter.html'
    return render(request, template, context)

def control_newsletter_list(request):
    newsletter = Newsletter.objects.all()

    paginator = Paginator(newsletter, 10)
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
    template = "control_panel/control_newsletter_list.html"
    return render(request, template, context)

def control_newsletter_detail(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    context = {
        'newsletter': newsletter,
    }
    template = 'control_panel/control_newsletter_detail.html'
    return render(request, template, context)


def control_newsletter_edit(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    if request.method == 'POST':
        form = NewsletterCreationForm(request.POST, instance=newsletter)

        if form.is_valid():
            newsletter = form.save()

            if newsletter.status == 'Published':
                #messages.success('', 'alert alert-success alert')
                subject = newsletter.subject
                body = newsletter.body
                from_email = settings.EMAIL_HOST_USER
                for email in newsletter.email.all():
                    print(type(email))
                    send_mail(subject=subject, from_email=from_email, recipient_list=[email.email], message=body,
                              fail_silently=True)
            return redirect('control_panel:control_newsletter_detail', pk=newsletter.pk)
    else:
        form = NewsletterCreationForm(instance=newsletter)
    context = {
        'form': form,
    }
    template = 'control_panel/control_newsletter.html'
    return render(request, template, context)

def control_newsletter_delete(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    if request.method == 'POST':
        form = NewsletterCreationForm(request.POST, instance=newsletter)

        if form.is_valid():
            newsletter.delete()
            return redirect('control_panel:control_newsletter_list')
    else:
        form = NewsletterCreationForm(instance=newsletter)

    context = {
        'form':form,
    }

    template = 'control_panel/control_newsletter_delete.html'
    return render(request, template, context)

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
    competition = Image.objects.get(name='DECA_Competition')
    scioly = Image.objects.get(name='about_scioly')
    context = {
     #   'banner': banner,
        'competition': competition,
        'scioly':scioly,
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

def term(request):
    return render(request, 'website/termsofuse.html')


from website.secret import *

@lockdown()
def science_olympiad_resources(request):
    if request.user.is_authenticated:
        return redirect(return_link())
    else:
        return redirect('/accounts/login/')
