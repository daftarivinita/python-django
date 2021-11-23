from django.shortcuts import render, redirect
from apps.log_and_register_app.models import User
from apps.book_app.models import *
from django.contrib import messages
# Create your views here.

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    current_user = User.objects.filter(id = (request.session['user_id']))[0]
    context= {
        "all_books": Book.objects.all(),
        "current_user":current_user,
        "all_user": User.objects.all()

    }
    return render(request, "book.html", context)
   

def create_book(request):
    print(request.session['user_id'])
    errors = Book.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/books')
    current_user = User.objects.filter(id = (request.session['user_id']))[0]
    new_book = Book.objects.create(
        title = request.POST['title'],
        desc=request.POST['description'],
        uploaded_by = current_user
    )
    return redirect('/books/')

def logout(request):
    request.session.flush()
    return redirect('/')

def book_detail(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    current_user = User.objects.filter(id = (request.session['user_id']))[0]
    context= {
        "current_book": Book.objects.filter(id= book_id)[0],
        "current_user":current_user,
        "all_user": User.objects.all()

    }

    return render(request, "book_detail.html", context)

def favorite(request, book_id):
    current_user = User.objects.filter(id = (request.session['user_id']))[0]
    current_book= Book.objects.filter(id =book_id)[0]
    print(current_user)
    print(current_book)
    current_user.liked_books.add(current_book)
    print(current_user.liked_books.add(current_book))

    return redirect('/books')

def unfavorite(request, book_id):
    current_user = User.objects.filter(id = (request.session['user_id']))[0]
    current_book= Book.objects.filter(id =book_id)[0]
    print(current_user)
    print(current_book)
    current_user.liked_books.remove(current_book)
    print(current_user.liked_books.remove(current_book))

    return redirect('/books')

def update(request, book_id):
    if request.method != "POST":
        return redirect("/books")
    print(1234567890)
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Book.objects.update_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
            print(key, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/books/{book_id}')
    else:
        current_user = User.objects.filter(id = (request.session['user_id']))[0]
        book_to_update = Book.objects.get(id=book_id)	# let's retrieve a single book,
        book_to_update.title = request.POST['title']
        book_to_update.desc = request.POST['description']	# update one/some of its field values
        book_to_update.save()
        return redirect ("/books")

def destroy(request, book_id):
    if request.method != "POST":
        return redirect("/books")
    book_to_delete = Book.objects.get(id=book_id)	# let's retrieve a single book,
    book_to_delete.delete()
    return redirect("/books")