from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from accounts.forms import RegistrationForm

# Create your views here.
def register(request):
    print(request.method)
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            instance = form.save()
            instance.save()
            print('valid')
    else:
        form = RegistrationForm()

        context = {
            'form': form,
        }
        return render(request, 'registration/reg_form.html', context)
    return redirect('website:index')