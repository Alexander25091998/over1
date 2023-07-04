from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('about/<str:user>/<int:age>', views.user),
    path('about/<str:user>', views.user_name)

]