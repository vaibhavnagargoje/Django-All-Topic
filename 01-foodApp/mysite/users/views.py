from django.shortcuts import render,redirect
# from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from .forms import RegistorForm
# Create your views here.



def registor(request):
    if request.method=="POST":
        form = RegistorForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}! Acount Created..')
            return redirect('login')
        
    else:

        form = RegistorForm()
    # form = AuthenticationForm()
    return render(request,'users/register.html',{'form':form})


    