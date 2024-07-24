from rest_framework import generics, response,status
from .models import  *
from .serializers import *


class CpuView(generics.ListCreateAPIView):
    serializer_class = CpuSerializer

    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        if brand:
            return Products.objects.filter(brand=brand, type='cpu')
        else:
            return Products.objects.filter(type='cpu')

class CpuViewEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = CpuSerializer

class GpuView(generics.ListCreateAPIView):
    serializer_class = GpuSerializer

    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        if brand:
            return Products.objects.filter(brand=brand, type='gpu')
        else:
            return Products.objects.filter(type='gpu')
        
    def perform_create(self, serializer):
        serializer.save(type='gpu')

class GpuViewEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.filter(type='gpu')
    serializer_class = GpuSerializer


class OrderAdd(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = PostOrderSerializer

class OrderView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = GetOrderSerializer

class OrderEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = GetOrderSerializer

class OrderItemsCreate(generics.CreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = PostOrderItemsSerializer
class BrandNamesListView(generics.ListCreateAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer

class BrandNamesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer