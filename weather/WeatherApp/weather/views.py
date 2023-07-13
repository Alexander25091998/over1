from django.shortcuts import render
import requests


def index(request):
    apiid = "8dccd4367e7a423e71b0d642cf108959"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + apiid
    city = 'Brest'
    res = requests.get(url.format(city))
    data = res.json()
    city_info = {
        "city": city,
        "temp": data["main"]["temp"],
        "icon": data["weather"][0]["icon"],
    }
    context = {"info": city_info}
    return render(request, 'weather/index.html', context)
