from django.contrib.messages.api import error
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def method_name(request):
    context = {
    "all_courses" : Course.objects.all(),
    
    }
    return render(request, "index.html", context)

def AddingCourse(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    # errors = Course.objects.basic_validator(request.POST)
    #     # check if the errors dictionary has anything in it
    # if len(errors) > 0:
    #     # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     # redirect the user back to the form to fix the errors
    #     return redirect('/')
    if request.method == "POST":
        new_course = Course.objects.create(name= request.POST['name'])
        new_description = Description.objects.create(content= request.POST['description'], course= new_course )
        
        print(new_course)
    
    return redirect('/')


def deleteAction(request, description_id):

    context = {
        "course_to_delete": Course.objects.get(id= description_id)
    }
   
    return render(request, "delete.html", context)

def goBack(request):
    return redirect('/')

def destroy(request, description_id):
    if request.method != "POST":
        return redirect('/')
    print(description_id)
    course_to_delete = Course.objects.get(id= description_id)
    
    course_to_delete.delete()
    return redirect('/')

def comment(request, course_id):
    context= {
    "course_to_comment": Course.objects.get(id = course_id)
    }
    return render(request, "comment.html", context)
    
   



def createComment(request, course_id):
    print(course_id)
    course = Course.objects.get(id = course_id)
    print(course, "@@@@@@@@@@@@@@@@@@@@")
    comments= Comment.objects.create(content =request.POST['comment'], course = course)
    #comment = Comment.objects.create(content= request.POST['comment'], course=Course.objects.get(id=course_id))
    return redirect(f"/{course_id}/comment")