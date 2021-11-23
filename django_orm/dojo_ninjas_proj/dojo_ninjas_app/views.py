from django.shortcuts import render, HttpResponse, redirect
from .models import *
def method_name(request):
    context= {
        "dojos": Dojo.objects.all(),
        
    }
    
    return render(request, "index.html",context)

def actionDojo(request):
   
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state = request.POST['state'])
    #request.session['dojo'] =Dojo.objects
    return redirect('/')


def actionNinja(request):
    new_ninja =Ninja.objects.create(first_name = request.POST['first_name'], last_name =request.POST['last_name'], dojo = Dojo.objects.get(id=request.POST['dojo']))
    return redirect('/')

def delete(request):
    id=request.POST['dojo']
    print("id: " + id)
    
    dojo_to_delete = Dojo.objects.get(id=id)	
    dojo_to_delete.delete()
    return redirect('/')

#   NINJA BONUS: Add a delete button next to each dojo name that deletes that dojo (and all associated ninjas) from the database