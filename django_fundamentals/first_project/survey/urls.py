from django.urls import path
from . import views

urlpatterns = [
path('', views.method_name),
path('new', views.method_name1),
]