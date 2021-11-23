from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse( "placeholder to later display a list of all blogs" )

def new(request):
    return HttpResponse('This is a a placeholder for the form for new blogs')

def create(request):
    return redirect('/') # to redirect we should make sure redirect is in import line

def show(request, number):
    return HttpResponse(f"The blog number is {number}")

def edit(request,number):
    return HttpResponse(f"Placeholder to edit blog{number}")

def destroy(request, number):
    return redirect('/')


def one_method(request):
    pass
def another_method(request, my_val):
    return HttpResponse(my_val)

def one_more(request, my_val, color):
    return HttpResponse(my_val, color)

def contact(request):
    return HttpResponse("this is a placeholder for conatct page")

def profile(request, person_number):
    return HttpResponse(f"this is a placeholder for {person_number}")

def person_profile(request, name):
    return HttpResponse(f"this is placeholder for my {name}")