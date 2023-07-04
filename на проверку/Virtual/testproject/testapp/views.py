from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):

    return render(request, 'base.html')


def about(request):
    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")
        print(name, date)
    contex = {
        "zap": "text1",
        "zap1": models.Mode1.objects.all()
    }
    return render(request, 'about.html', contex)


def user(request, user, age):
    return HttpResponse(f'<h2>Имя {user}, Возраст {age}<h2>')


def user_name(request, user):
    return HttpResponse(f'<h2>Имя {user}<h2>')


def contacts(request):
    return render(request, 'contacts.html')