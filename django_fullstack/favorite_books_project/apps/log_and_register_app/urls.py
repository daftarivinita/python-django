from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register), #GET request to display all objects' info starting at a different root
    path('success', views.success), #GET request to display form to create an object
    path('login', views.login), #POST request to create an object
    path('logout', views.logout), #GET request to display a specific object's info
    # path('objects/<int:object_id>/edit', views.edit_object), #GET request to display form to update a specific object
    # path('objects/<int:object_id>/update', views.update_object), #POST request to update a specific object
    # path('objects/<int:object_id>/destroy', views.delete_object), #POST request to delete a specific object
]