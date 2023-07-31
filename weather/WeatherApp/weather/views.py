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
        return redirect('/')

    form = CityForm
    context = {"all_info": all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
# {'city': cities, "temp": data["main"]["temp"], "icon": data["weather"][0]["icon"] }


class NewsDeleteView(DeleteView):
    model = City
    success_url = 'http://127.0.0.1:8000'
    template_name = 'weather/index.html'


class NewsDeleteViewH(DeleteView):
    model = CityHistory
    success_url = 'http://127.0.0.1:8000'
    template_name = 'weather/history.html'


def history(request):
    history_cities = []
    history_cities.clear()
    for city in City.objects.all():
        CityHistory.objects.create(id=city.id, name=city.name)
    City.objects.all().delete()
    for city in CityHistory.objects.all():
        city_info = {
            'city': city.name
        }
        history_cities.append(city_info)

    context = {"hist_info": history_cities}
    return render(request, 'weather/history.html', context)

# for obj in Table1.objects.all():
#     new_obj = Table2.objects.create(
#         field1=obj.field1,
#         field2=obj.field2,
#         field3=obj.field3,
#     )
