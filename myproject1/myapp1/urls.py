from django.urls import path, include
from .views import sayHello, sayH1, car_list, get_brands, get_brands_by_country, get_vehicle_by_brand, get_vehicle_by_brands

urlpatterns = [
    path('hello', sayHello),
    path('h1', sayH1),
    path('cars/', car_list),
    path('cars/brand', get_vehicle_by_brand),
    path('cars/brands', get_vehicle_by_brands),
    path('brands', get_brands),
    path('brands/country', get_brands_by_country),

]