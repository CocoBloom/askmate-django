from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Virág',
        'title': 'First Question',
        'content': 'This is my first question  in Django',
        'date_posted': 'Apr 2, 2020'
    },
    {
        'author': 'Coco',
        'title': 'First Coco',
        'content': 'This is my Coco in Django',
        'date_posted': 'Apr 1, 2020'
    }
]


def home(request):
    context = {
        'posts': posts,
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