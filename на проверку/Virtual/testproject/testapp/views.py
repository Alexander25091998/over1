from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Главная<h1>')


def about(request):
    return HttpResponse('<h2>Главная<h2>')


def user(request, user, age):
    return HttpResponse(f'<h2>Имя {user}, Возраст {age}<h2>')


def user_name(request, user):
    return HttpResponse(f'<h2>Имя {user}<h2>')