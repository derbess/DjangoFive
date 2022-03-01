from rest_framework.serializers import ModelSerializer

from basket.models import Basket


class BasketSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'

