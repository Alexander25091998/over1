from django.shortcuts import render
from .models import City
import requests


def index(request):
    apiid = "8dccd4367e7a423e71b0d642cf108959"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + apiid
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name))
        data = res.json()
        city_info = {
            "city": city.name,
            "temp": data["main"]["temp"],
            "icon": data["weather"][0]["icon"],
        }
        all_cities.append(city_info)
    context = {"all_info": all_cities}
    return render(request, 'weather/index.html', context)
# {'city': cities, "temp": data["main"]["temp"], "icon": data["weather"][0]["icon"] }