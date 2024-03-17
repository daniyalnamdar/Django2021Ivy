from django.urls import path
from . import views

urlpatterns = [

    path('', views.projects),
    path('project/<int:pk>/', views.project),
]
