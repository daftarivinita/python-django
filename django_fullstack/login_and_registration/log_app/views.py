from django.contrib.messages.api import error
from django.shortcuts import render, redirect
import bcrypt


from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request, "login.html")

def register(request):
    if request.method == "GET":
        return redirect("/")
    
    errors = User.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/') 
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    new_user = User.objects.create(first_name= request.POST['first_name'],last_name= request.POST['last_name'],birthdate = request.POST['birthdate'], email= request.POST['email'],password= pw_hash)
    request.session['user_id'] = new_user.id
    return redirect("/success")

    
def success(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please login to access!") 
        return redirect('/')
    print(request.session['user_id'])
    user = User.objects.get(id = request.session['user_id'])
    #messages.success(request, "You are successfully login!")
    context = {
        "current_user": user
        }
    print(context)
    return render(request, "success.html", context)
    
def login(request):
    if request.method == "GET":
        return redirect("/")
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    this_user = User.objects.filter(email = request.POST['email'])[0]
    request.session['user_id'] = this_user.id
    return redirect("/success")
    
def logout(request):
    request.session.flush()
    return redirect('/')
    

    
    
    

    

    
   
        
    
    

    
    
    
    
    

    