from django.urls import path, include
from rest_framework import routers

from api.views import CategoryAPIViewset, ProductAPIViewset

router = routers.DefaultRouter()
router.register(r'category', CategoryAPIViewset, basename='category')
router.register(r'product', ProductAPIViewset, basename='product')


urlpatterns = [
]

urlpatterns += router.urls