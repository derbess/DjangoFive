from rest_framework.routers import DefaultRouter

from basket.views import BasketAPIViewset, BasketProductAPIViewset

router = DefaultRouter()
router.register(r'basket', BasketAPIViewset, basename='basket')
router.register(r'product', BasketProductAPIViewset, basename='basket_product')

urlpatterns = [

]
urlpatterns += router.urls
print(router)
