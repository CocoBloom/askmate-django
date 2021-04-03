from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Juhuu page'
    }
    return render(request, 'askmate/home.html', context)


def about(request):
    return render(request, 'askmate/about.html')


def login(request):
    return HttpResponse("This is the Login page")


def logout(request):
    return HttpResponse("This is the Logout page")


def registration(request):
    return HttpResponse("This is the Registration page")