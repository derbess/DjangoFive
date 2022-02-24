from django.urls import path
from rest_framework import routers

from api.views import CategoryAPIViewset

router = routers.DefaultRouter()
router.register(r'category', CategoryAPIViewset, basename='category')

urlpatterns = [
    # path('/categories', )
]

urlpatterns += router.urls