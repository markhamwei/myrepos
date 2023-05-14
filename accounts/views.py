from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def register_page(request):
    if(request.method == "POST"):
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/login")
        return render(request, 'account/register.html', {'form':form})
    
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form':form})