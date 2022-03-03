from django.shortcuts import render
from rest_framework import viewsets, generics
# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from basket.models import Basket, BasketProduct
from basket.serializers import BasketSerializer, BasketProductSerializer


class BasketAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class BasketProductAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = BasketProductSerializer

    def get_queryset(self):
        if(self.request.user.is_staff == True):
            return BasketProduct.objects.all()
        return BasketProduct.objects.filter(basket_id = 1 )