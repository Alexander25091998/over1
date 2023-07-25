from django.urls import path
from .models import City
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete'),
    path('<int:pk>/deleteH', views.NewsDeleteViewH.as_view(), name='deleteH'),
    path('history/', views.history, name='history'),
]