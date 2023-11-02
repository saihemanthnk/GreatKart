from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST) # request.post contains all the field values 
        if form.is_valid():
            first_name = form.cleaned_data['first_name'] 
            last_name = form.cleaned_data['last_name'] 
            email  = form.cleaned_data['email'] 
            phone = form.cleaned_data['phone'] 
            password = form.cleaned_data['password']
            username = email.split('@')[0] 
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password) 
            user.phone = phone 
            user.save() 
            messages.success(request,'Registration successful')
            return redirect('register')
        else:
            return render(request,'accounts/register.html',{"form":form})
    else:

        form = RegistrationForm() 
        return render(request,'accounts/register.html',{"form":form})


def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return render(request,'accounts/logout.html')
