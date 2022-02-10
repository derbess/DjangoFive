from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Brand
from .serializers import BrandSerializer
# Create your views here.


class DataList(APIView):
    def get(self, request):
        return Response({'data': "Derbes Utebaliyev"})
    def post(self, request):
        title = request.data['title']
        print(title)
        return Response({'data2': "Derbes Utebaliyev"})

class BrandAPIView(APIView):
    def get(self, request):
        list1 = Brand.objects.all()
        q = BrandSerializer(list1, many=True)

        print(q, type(q), q.data, sep='\n')
        return Response({"data": q.data})

    def post(self, request):
        serializer = BrandSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"data": serializer.data})

class BrandAPIViewDetailed(APIView):
    def put(self, request, pk):
        brand = Brand.objects.get(id=pk)
        serializer = BrandSerializer(data=request.data, instance=brand)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"data": serializer.data})

    def delete(self):
        pass
