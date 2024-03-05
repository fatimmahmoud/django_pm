from django.urls import path, include
from . import views

 
urlpatterns = [
    #المفترض بين ال" نضع الرابط 
    path('', views.ProjectListView.as_view(), name='project_List'),
    path('project/creat', views.ProjectCreatView.as_view(), name='project_creat'),
    path('project/edit/<int:pk>', views.ProjectUpdateView.as_view(), name='project_update'),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('task/creat', views.TaskCreatView.as_view(), name='task_creat'),
    path('task/edit/<int:pk>', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='task_delete'),
]

