from django.contrib.messages.api import error
from django.shortcuts import render, redirect
import bcrypt


from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request, "login.html")

def register(request):
    # if request.method == "GET":
    #     return redirect("/")

    print(request.POST['birthdate'])
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = User.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
    # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/') # redirect the user back to the form to fix the errors
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    
    new_user = User.objects.create(first_name= request.POST['first_name'],last_name= request.POST['last_name'],birthdate = request.POST['birthdate'], email= request.POST['email'],password= pw_hash)
    request.session['user_id'] = new_user.id
    request.session['first_name']= new_user.first_name
    return redirect("/books")

    
    

def success(request):
    if 'user_id' not in request.session:
       return redirect('/')
    print(request.session['user_id'])
    user = User.objects.get(id = request.session['user_id'])
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
    
    print(this_user)
    if bcrypt.checkpw(request.POST['password'].encode(), this_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
        #request.session['User_id'] = target_user.id
        request.session['user_id'] = this_user.id
        request.session['first_name']= this_user.first_name
        return redirect("/books")
    messages.error(request, "Please enter a valid email and password!")   
    return redirect('/')
    
    
# redirect the user back to the form to fix the errors
    
    


    
    

def logout(request):
    
    request.session.flush()
    return redirect('/')