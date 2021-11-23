from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    context= {
        "user": User.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    if request.method == "POST":
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address = request.POST['email'], age= request.POST['age'])
    return redirect('/')

#when I dont fill age it throws an error. How do I fix it