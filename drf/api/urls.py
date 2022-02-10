from django.urls import path
from .views import DataList, BrandAPIView, BrandAPIViewDetailed
urlpatterns = [
    path('data/', DataList.as_view()),
    path('brands/', BrandAPIView.as_view()),
    path('brands/<int:pk>', BrandAPIViewDetailed.as_view()),

]