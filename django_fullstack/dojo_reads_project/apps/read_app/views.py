from django.shortcuts import redirect, render
from django.contrib.messages.api import error

from datetime import date
from django.contrib import messages
from .models import *
# Create your views here.
def book(request):
    if 'user_id' not in request.session:
       return redirect('/')
    print(request.session['user_id'])
    user = User.objects.get(id = request.session['user_id'])
    context = {
        "current_user": user,
        "all_book":Book.objects.all(),
        "recent_review": Review.objects.order_by('created_at').reverse()[:3]
    }
    print(context)
    return render(request,"book.html", context)
def add_book(request):
    if 'user_id' not in request.session:
       return redirect('/')
    print(request.session['user_id'])
    user = User.objects.get(id = request.session['user_id'])
    context = {
        "current_user": user,
        "all_author" : Author.objects.all()
    }
    return render(request,"add.html", context)
def create_book(request):
    if request.method != "POST":
        return redirect("/")
# pass the post data to the method we wrote and save the response in a variable called errors
    errors = Book.objects.basic_validator(request.POST)
     # check if the errors dictionary has anything in it
    if len(errors) > 0:
     # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        
    review_errors = Review.objects.basic_validator(request.POST)
    if len(review_errors) > 0:
        for k, v in review_errors.items():
            messages.error(request, v)
        
    author_errors = Author.objects.basic_validator(request.POST)
    if len(author_errors) > 0:
        for k, v in author_errors.items():
            messages.error(request, v)
        return redirect("/books/new")
    # redirect the user back to the form to fix the errors
    user = User.objects.get(id = request.session['user_id'])
    current_author = Author.objects.filter(name = request.POST['new_author'])
    if not current_author:
        current_author = Author.objects.create(name = request.POST['new_author'])
    else:
        current_author = current_author[0]
    new_book = Book.objects.create(title= request.POST['title'], author=current_author)
    new_review= Review.objects.create(content=request.POST['review'] , rating=request.POST['rating'],book = new_book, reviewed_by =user )
   
    
    bookid = new_book.id
    return redirect(f'/books/{bookid}')
def view_book(request, book_id):
    if 'user_id' not in request.session:
       return redirect('/')
    user = User.objects.get(id = request.session['user_id'])
    current_book = Book.objects.filter(id = book_id)[0]
    context = {
        "current_user": user,
        "current_book": current_book
    }
    return render(request,"book_detail.html", context)



def create_review(request, book_id):
    if request.method != "POST":
        return redirect("/")
    book = Book.objects.filter(id = book_id)[0]
    user = User.objects.get(id = request.session['user_id'])
    new_review= Review.objects.create(content=request.POST['review'] , rating=request.POST['rating'],book = book, reviewed_by =user )
    return redirect(f'/books/{book.id}')


def delete_review(request, book_id, review_id):
    # if request.method != "POST":
    #         return redirect(f"/books/{review_id}")
    # print(book_id)
    # print(review_id)
    print(Review.objects.all())
    review_to_delete = Review.objects.get(id=review_id)	# let's retrieve a single review,
    review_to_delete.delete()
    #bookid = book_id
    return redirect(f'/books/{book_id}')
    
    




    