from django.urls import path
from . import views

urlpatterns = [
path('', views.method_name),
path('action_page/dojo', views.actionDojo),
path('action_page/ninja', views.actionNinja),
path('delete', views.delete),
]
