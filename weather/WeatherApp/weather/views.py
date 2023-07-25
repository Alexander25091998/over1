from django.shortcuts import render, redirect
from .models import City, CityHistory
import requests
from .forms import CityForm
from django.views.generic import DetailView, DeleteView


def yes(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    return render(request, 'weather/baze.html')


def index(request):
    apiid = "8dccd4367e7a423e71b0d642cf108959"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + apiid
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name))
        data = res.json()
        city_info = {
            "id": city.id,
            "city": city.name,
            "temp": data["main"]["temp"],
            "icon": data["weather"][0]["icon"],
        }
        all_cities.append(city_info)

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        for citys in City.objects.all():
            for city in CityHistory.objects.all():
                if city == citys:
                    print('есть')
                else:
                    CityHistory.objects.create(name=citys.name)
        return redirect('/')

    form = CityForm
    context = {"all_info": all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
# {'city': cities, "temp": data["main"]["temp"], "icon": data["weather"][0]["icon"] }


class NewsDeleteView(DeleteView):
    model = City
    success_url = 'http://127.0.0.1:8000/yes'
    template_name = 'weather/index.html'


class NewsDeleteViewH(DeleteView):
    model = CityHistory
    success_url = 'http://127.0.0.1:8000'
    template_name = 'weather/history.html'


def history(request):
    cities = CityHistory.objects.all()
    history_cities = []
    for city in cities:
        if city not in cities:
            city_info = {
                'id': city.id,
                "city": city.name,
            }
            history_cities.append(city_info)

    context = {"hist_info": history_cities}
    return render(request, 'weather/history.html', context)

