from django.urls import path
from . import views

urlpatterns = [
path('', views.method_name),
path('addingCourse', views.AddingCourse),
path('<int:description_id>', views.deleteAction),
path('goback', views.goBack),
path('<int:description_id>/delete', views.destroy),
path('<int:course_id>/comment', views.comment),   #path to render comment file
path('comment/<int:course_id>/create', views.createComment)

]
