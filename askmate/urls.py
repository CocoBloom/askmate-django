from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Main page'),
    path('about/', views.about, name='About page'),
]
