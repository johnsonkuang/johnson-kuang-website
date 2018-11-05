from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from accounts.forms import RegistrationForm

# Create your views here.
def register(request):

    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Success!',
                             'alert alert-success alert-dismissible')
            return redirect('website:index')
        else:
            messages.warning(request,
                             'Please fix the following errors: ' + str(form.errors),
                             'alert alert-warning alert-dismissible')
            context = {
                'form': form,
            }
            return render(request, 'registration/reg_form.html', context)

    else:
        form = RegistrationForm()

        context = {
            'form': form,
        }
        return render(request, 'registration/reg_form.html', context)
