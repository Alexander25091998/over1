from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>Hello</h4>')


def user(request):
    return HttpResponse('<a href="https://github.com/Alexander25091998">CCылка на мой GitHub</a>')


