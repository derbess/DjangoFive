from django.urls import path
from rest_framework import routers

from api.views.views import *
from api.views.viewset import *


router = routers.DefaultRouter()
router.register(r'brand', BrandAPIViewset, basename='brand')
router.register(r'vehicle', VehicleAPIViewset, basename='vehicle')

urlpatterns = [
    # path('data/', DataList.as_view()),
    # path('brands/', BrandAPIView.as_view()),
    # path('brands/<int:pk>', BrandAPIViewDetailed.as_view()),
    # path('per/', BrandAPIViewset.as_view({'get': 'list'})),
    # path('brands/<int:pk>', BrandDetailUpdateDeleteAPIView.as_view()),
    # path('vehicle/', VehicleListCreateAPIView.as_view()),
    # path('vehicle/<int:pk>', VehicleDetailUpdateDeleteAPIView.as_view()),
    # path('vehicle/year/', VehicleListAPIView.as_view() )

]

urlpatterns += router.urls