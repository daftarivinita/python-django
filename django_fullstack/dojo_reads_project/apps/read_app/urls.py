from django.urls import path
from . import views

urlpatterns = [
    path('', views.book), #GET request to display all objects' info starting at root
    #path('objects', views.object), #GET request to display all objects' info starting at a different root
    path('new', views.add_book), #GET request to display form to create an object
    path('create', views.create_book), #POST request to create an object
    path('<int:book_id>/reviews', views.create_review), #POST request to create an object
    path('<int:book_id>', views.view_book), #GET request to display a specific object's info
    #path('objects/<int:object_id>/edit', views.edit_object), #GET request to display form to update a specific object
    #path('objects/<int:object_id>/update', views.update_object), #POST request to update a specific object
    path('<int:book_id>/<int:review_id>/destroy', views.delete_review), #POST request to delete a specific object
]