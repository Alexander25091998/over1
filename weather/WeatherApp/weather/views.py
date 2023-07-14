from django.shortcuts import render
from .models import City
import requests


def index(request):
    for e in City.objects.all():
        cit = City.objects.all()
        city = e
        apiid = "8dccd4367e7a423e71b0d642cf108959"
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + apiid
        res = requests.get(url.format(city))
        data = res.json()
        city_info = {
            "city": city,
            "temp": data["main"]["temp"],
            "icon": data["weather"][0]["icon"],
        }
        return render(request, 'weather/index.html',  {'city': cit, "city_info": city_info})
