from django.contrib.messages.api import error
from django.shortcuts import render, redirect
from datetime import date


from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "all_the_shows": Tvshow.objects.all()
    }
    return render(request, "show.html", context)

def newForm(request):
    return render(request, "index.html")

def create(request):
    errors = Tvshow.objects.basic_validator(request.POST)
    print(request.POST)
    print(errors)
    print(len(errors))
    if len(errors) > 0:
    # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
    # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        newshow =Tvshow.objects.create(title= request.POST['title'], description = request.POST['description'] , release_date= request.POST['release_date'],network= request.POST['network'] )
        return redirect('/shows/'+ str(newshow.id))


def showsInfo(request, id):
    context={
        "shows": Tvshow.objects.get(id=id)
    }
    return render(request, "showsInfo.html", context)

def edit(request, id):
    context= {
        "new_show": Tvshow.objects.get(id=id)
    }
   
    return render(request, "edit.html", context)

def update(request, id):
    errors = Tvshow.objects.update_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/" + str(id) + "/edit")
    else:
        new_show= Tvshow.objects.get(id= id)
        new_show.title= request.POST['title']
        new_show.description = request.POST['description'] 
        new_show.release_date= request.POST['release_date']
        new_show.network= request.POST['network']
        new_show.save()
        return redirect('/shows/' + str(id))                

def destroy(request, id):
    show_to_destroy= Tvshow.objects.get(id= id)
    show_to_destroy.delete()
    return redirect('/shows')


