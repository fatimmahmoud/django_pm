from django.urls import path, include
from . import views

 
urlpatterns = [
    #المفترض بين ال" نضع الرابط 
    path('', views.ProjectListView.as_view(), name='project_List'),
    path('project/creat', views.ProjectCreatView.as_view(), name='project_creat'),

]

