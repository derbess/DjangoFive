from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Car, Brand, Vehicle
import json

# Create your views here.

menu_list = ["header", "menu", "first page", "about", "footer"]

def sayHello(request):
    return render(request, 'hello.html', {"title": "Главная страница",
                                          "page": "Страница для hello",
                                          "menu_list": menu_list}
                  )

def sayH1(request):
    return render(request, 'helloh1.html', {"title": "Вторая страница",
                                            "page": "Страница для helloh1",
                                            "menu_list": menu_list
                                            }
                  )

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {
        "title": "Вторая страница",
        "cars": cars
    })

def get_brands(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {
        "title": "Вторая страница",
        "brands": brands
    })

def get_brands_by_country(request):
    brands = Brand.objects.filter(country="Germany")
    return render(request, 'brand_list.html', {
        "title": "Вторая страница",
        "brands": brands
    })

def get_vehicle_by_brand(request):
    brand = Brand.objects.get(name="Mercedes")
    cars = brand.get_vehicles.all()
    # cars = brand.vehicle_set
    return render(request, 'car_list.html', {
        "title": "Вторая страница",
        "cars": cars
    })

def get_vehicle_by_brands(request):
    cars = []
    brands = Brand.objects.filter(name__in=['Audi', 'Mercedes', 'BMW'])
    for brand in brands:
        for car in brand.get_vehicles.all():
            cars.append(car)
    print(cars)
    return render(request, 'car_list.html', {
            "title": "Вторая страница",
            "cars": cars
        })

# все машины после 2000
# все машины сортировать по году
# все брэнды которые начинаются на "L"
# все машины из Германии
