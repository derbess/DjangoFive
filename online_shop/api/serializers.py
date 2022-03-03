from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductShortSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'articule', 'currency', 'count', 'description')


class ProductSerializer(ProductShortSerializer):
    category = CategorySerializer(read_only=True)
    class Meta(ProductShortSerializer.Meta):
        fields = ProductShortSerializer.Meta.fields + ('category',)