from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import LoginForm, RegisterForm ,LoginForm
# Create your views here.
def index(request):
    form = RegisterForm()
    log_form = LoginForm()
    context = { 
        "regForm": form ,
        "logForm": log_form
        }
    return render(request, "index.html", context)

def create_user(request):
    if request.method != "POST":
        return redirect('/')
    reg_form = RegisterForm(request.POST)
    if reg_form.is_valid():
        
        new_user = reg_form.save()

        return redirect('/home')

    else:
        context = { 
        "regForm": RegisterForm(),
        "logForm":  LoginForm()
        }
        return render(request, 'index.html', context)

        #we can do User.create()