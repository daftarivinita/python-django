from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('shows', views.shows),
path('shows/new', views.newForm),
path('shows/create',views.create),
path('shows/<int:id>', views.showsInfo),
path('shows/<int:id>/edit', views.edit),
path('shows/<int:id>/update',views.update),
path('shows/<int:id>/destroy',views.destroy),

]






# /shows/<id>/update - POST - method should update the specific show in the database, then redirect to /shows/<id>

# /shows/<id>/destroy - POST - method should delete the show with the specified id from the database, then redirect to /shows