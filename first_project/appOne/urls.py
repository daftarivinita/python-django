from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('blogs/', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>' , views.show),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
    path('bears', views.one_method),
    path('bears/<int:my_val>', views.another_method),
    path('<int:my_val>/<str:color>', views.one_more),
    path('contact', views.contact),
    path('profile/<int:person_number>',views.profile),
    path('profile/<str:name>', views.person_profile),
]
