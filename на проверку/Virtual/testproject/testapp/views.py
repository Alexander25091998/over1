from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')


def user(request, user, age):
    return HttpResponse(f'<h2>Имя {user}, Возраст {age}<h2>')


def user_name(request, user):
    return HttpResponse(f'<h2>Имя {user}<h2>')

def contacts(request):
    return render(request, 'contacts.html')