from django.urls import path
from . import views

urlpatterns = [
path('register', views.method_name),
path('login', views.method_name1),
path('users/new', views.method_name2),
path('users', views.method_name3),
]
