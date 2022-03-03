from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *


class CategoryAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return CategorySerializer

    def get_queryset(self):
        # if(self.kwargs.get('pk')):
        #     return

        return Category.objects.all()
    

class ProductAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if (self.kwargs.get('pk')):
            return ProductSerializer
        return ProductShortSerializer

    def get_queryset(self):
        return Product.objects.all()

