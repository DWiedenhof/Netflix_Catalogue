from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('title/', views.title),
]

