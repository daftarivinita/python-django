from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
def index(request):
    context = {
        "all_foods": Food.objects.all()
    }
    return render(request, "index.html", context)



def create_food(request):
    if request.method != "POST":
        return redirect("/")
    new_food = Food.objects.create(name = request.POST['food_name'])
    return redirect('/')

def create_food_ajax(request):
    if request.method != "POST":
        return redirect("/")
    new_food = Food.objects.create(name = request.POST['food_name'])
    context = {
        "all_foods": Food.objects.all()
    }
    return render(request, "table_snippet.html", context)
   