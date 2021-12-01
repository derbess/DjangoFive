from django.urls import path, include
from .views import sayHello, sayH1, car_list

urlpatterns = [
    path('hello', sayHello),
    path('h1', sayH1),
    path('cars/', car_list)
]