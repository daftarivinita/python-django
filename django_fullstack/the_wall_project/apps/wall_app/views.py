from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from apps.log_and_register_app.models import User
from apps.wall_app.models import *
# Create your views here.
def wall(request):
    # print(request.session['user_id'])
    if "user_id" not in request.session:
        return redirect('/')
    current_user = User.objects.get(id =request.session['user_id'] )
    #all_message = Message.objects.all()
    all_message = Message.objects.all().order_by('-created_at')

    all_comment = Comment.objects.all()
    context = {
        "user":current_user,
        "messages": all_message,
        "comments":all_comment,
        "all_user":User.objects.all(),
    }
    return render(request, "index1.html", context)

def postmessage(request):
    if 'user_id' not in request.session or request.method != "POST":
        return redirect('/')

    current_user = User.objects.get(id =request.session['user_id'] )
    new_message = Message.objects.create(
        content=request.POST['messages'],
        posted_by = current_user
    )
    #current_user.messages = new_message
    request.session['message_id']= new_message.id
    return redirect('/wall')

def postcomment(request, message_id):
    if 'user_id' not in request.session or request.method != "POST":
        return redirect('/')
    # print(request.session['message_id'])
   
    current_user = User.objects.get(id =request.session['user_id'] )
    current_message= Message.objects.get(id =message_id)
    new_comment = Comment.objects.create(
        content = request.POST['comment'],
        commented_by = current_user,
        on_message = current_message,
    )
    print(new_comment.on_message)
    print(new_comment.on_message.content)
    request.session['comment_id']= new_comment.id
    return redirect('/wall/')
    


def logoff(request):
    request.session.flush()
    return redirect('/')

def delete_message(request, message_id):
    if request.method != "POST":
        return redirect('/')
    message_to_delete = Message.objects.filter(id = message_id)[0]
    message_to_delete.delete()
    return redirect('/wall/')

def delete_comment(request, comment_id):
    if request.method != "POST":
        return redirect('/')
    comment_to_delete = Comment.objects.filter(id = comment_id)[0]
    comment_to_delete.delete()
    return redirect('/wall/')
    
    

