from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView

from django.db.models import Value, FloatField, Prefetch
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
            return ProductRatingSerializer
        elif (self.request.method == "POST"):
            return ProductCreateSerializer
        return ProductSerializer

    def get_queryset(self):
        if(self.kwargs.get('pk')):
            pk = self.kwargs.get('pk')
            product = Product.objects.get(id=pk)
            ratings = Rating.objects.filter(product = product)
            avg = 0
            for item in ratings:
                avg = avg + item.grade
            # return Product.objects.get(id=pk).annotate(rating=Value(avg/len(ratings), output_field=FloatField()))
            p = Product.objects.prefetch_related(Prefetch('rating_set', queryset=Rating.objects.filter(product = product)))
            print(p.rating_set[0])
            return p
        return Product.objects.all()
        # App.objects.prefetch_related(Prefetch('rating_set', queryset=Rating.objects.filter(user=self.request.user))

class ProductAdd():
    pass


class RatingAPIView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    serializer_class = RatingSerializer
    # queryset = Rating.objects.all()

    def get_queryset(self):
        return Rating.objects.all()






