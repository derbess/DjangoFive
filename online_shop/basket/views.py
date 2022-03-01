from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from basket.models import Basket
from basket.serializers import BasketSerializer


class BasketAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer