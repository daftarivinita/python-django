from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
all_the_authors = Author.objects.all()
all_the_books = Book.objects.all()
def index(request):
    context = {
        "all_books": all_the_books
    }
    if request.method == "POST":
        context = {
            "all_books": request.POST['all_the_books']
            }
    return render(request, "index.html", context)

def bookinfo(request, num):
    context = {
        "new_book": Book.objects.get(id = num),
        "all_author":all_the_authors
    }
    if request.method == "POST":
        context = {
            "all_author": request.POST[all_the_authors]
        }
    return render(request, "book.html", context)

def addingbook(request):
    Book.objects.create(title=request.POST['title'], desc= request.POST['desc'] )
    return redirect('/')

def addingauthors(request, bookid):
    author_id = request.POST['allauthor']
    author = Author.objects.get(id = author_id)
    print(bookid)
    print(author)
    Book.objects.get(id = bookid).authors.add(author)
    return redirect('/book/' + str(bookid))


def author(request):
    context={
        "all_authors": all_the_authors
    }
    if request.method == "POST":
        context = {
            "all_author": request.POST[all_the_authors]
        }
    return render(request, "authors.html", context)

def authorinfo(request, num):
    context= {
        "new_author":Author.objects.get(id=num),
        "all_books": all_the_books
    }
    return render(request, "newauthor.html", context)

def addingbooktoauthor(request, authorID):
    bookID = request.POST["allbook"]  #receive the id fromrequest.post in form target value
    book= Book.objects.get(id=bookID)  # got the object with that id
    Author.objects.get(id= authorID).books.add(book) #adding the id
    return redirect("/author/" + str(authorID))