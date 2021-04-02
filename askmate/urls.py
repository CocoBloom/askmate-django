from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Main page'),
    path('about/', views.about, name='About page'),
    path('login/', views.login, name='Login page'),
    path('registration/', views.registration, name='Reg page'),
    path('logout', views.logout, name='Logout page'),
]
