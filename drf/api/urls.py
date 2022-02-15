from django.urls import path
from .views import *
urlpatterns = [
    # path('data/', DataList.as_view()),
    # path('brands/', BrandAPIView.as_view()),
    # path('brands/<int:pk>', BrandAPIViewDetailed.as_view()),
    path('brands/', BrandListCreateAPIView.as_view()),
    path('brands/<int:pk>', BrandDetailUpdateDeleteAPIView.as_view()),
    path('vehicle/', VehicleListCreateAPIView.as_view()),
    path('vehicle/<int:pk>', VehicleDetailUpdateDeleteAPIView.as_view()),
    path('vehicle/year/', VehicleListAPIView.as_view() )

]