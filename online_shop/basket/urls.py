from rest_framework.routers import DefaultRouter

from basket.views import BasketAPIViewset

router = DefaultRouter()
router.register(r'', BasketAPIViewset, basename='basket')

urlpatterns = [

]

urlpatterns += router.urls