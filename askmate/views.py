from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("This is the Home page")


def about(request):
    return HttpResponse("This is the About page")


def login(request):
    return HttpResponse("This is the Login page")


def logout(request):
    return HttpResponse("This is the Logout page")


def registration(request):
    return HttpResponse("This is the Registration page")