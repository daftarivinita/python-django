from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall), #GET request to display all objects' info starting at root
    # path('objects', views.object), #GET request to display all objects' info starting at a different root
    # path('objects/new', views.add_object), #GET request to display form to create an object
    path('postmessages', views.postmessage),
    path('<int:message_id>/postcomments', views.postcomment), #POST request to create an object
    path('logoff', views.logoff), #GET request to display a specific object's info
    path('<int:message_id>/deletemessage', views.delete_message),
    path('<int:comment_id>/deletecomment', views.delete_comment), 
]