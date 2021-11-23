from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('farm/submit', views.farm_submit),
path('cave/submit', views.cave_submit),
path('house/submit', views.house_submit),
path('casino/submit', views.casino_submit),
path('reset', views.reset),
]
