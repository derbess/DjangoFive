from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

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