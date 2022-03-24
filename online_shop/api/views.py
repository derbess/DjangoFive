from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .service import ProductFilter


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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_serializer_class(self):
        # if(self.request.method == "POST"):
        #     print("PPPPP")
        if (self.kwargs.get('pk')):
            return ProductSerializer
        elif (self.request.method == "POST"):
            return ProductCreateSerializer
        return ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class ProductAdd():
    pass

