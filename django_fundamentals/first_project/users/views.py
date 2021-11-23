from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def method_name(request):
    return HttpResponse("placeholder for users to create a new user record")
def method_name1(request):
    return HttpResponse("placeholder for users to log in")
def method_name2(request):
    return redirect('/register')
def method_name3(request):
    return HttpResponse( "placeholder to later display all the list of users")