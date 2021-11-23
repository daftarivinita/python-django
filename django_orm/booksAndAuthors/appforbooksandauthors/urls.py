from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('book/<int:num>', views.bookinfo),  
path('add/book', views.addingbook),
path('book/add/<int:bookid>', views.addingauthors), #adding author to book
path('author', views.author),
path('author/<int:num>', views.authorinfo),
path('author/<int:authorID>/add', views.addingbooktoauthor)


]

