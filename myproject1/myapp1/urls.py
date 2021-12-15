from django.urls import path
from .views.views import sayHello, sayH1, car_list, get_brands, get_brands_by_country, get_vehicle_by_brand, \
    get_vehicle_by_brands, get_vehicle_by_brand_after, get_vehicle_by_name_start, get_vehicle_by_country

from .views.cbv import BrandListView


urlpatterns = [
    path('hello', sayHello),
    path('h1', sayH1),
    path('cars/', car_list),
    path('cars/brand', get_vehicle_by_brand),
    path('cars/brands', get_vehicle_by_brands),
    path('brands', get_brands),
    path('brands/country', get_brands_by_country),
    path('cars/year', get_vehicle_by_brand_after),
    path('cars/like', get_vehicle_by_name_start),
    path('cars/country', get_vehicle_by_country),

    path('cbv/brands', BrandListView.as_view())

]