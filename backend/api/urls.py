from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('todos/', views.getToDos, name='todos'),
    path('todos/<str:pk>', views.getToDo, name='todo'),
]

