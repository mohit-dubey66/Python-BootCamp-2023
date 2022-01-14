from django.urls import path,include
from projects import views
urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('project-form', views.createProject, name="project-form"),
    path('update-form/<str:pk>/', views.updateProject, name="update-form"),
    path('delete-form/<str:pk>/', views.deleteProject, name="delete-form"),
]