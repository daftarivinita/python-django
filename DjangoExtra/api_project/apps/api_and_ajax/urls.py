from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('food/create', views.create_food),
path('food/create_ajax', views.create_food_ajax),
]
