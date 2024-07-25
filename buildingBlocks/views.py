from rest_framework import generics, response,status
from .models import  *
from .serializers import *
from rest_framework.exceptions import ValidationError

class CpuView(generics.ListCreateAPIView):
    serializer_class = CpuSerializer

    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        if brand:
            return Products.objects.filter(brand=brand, type='cpu')
        else:
            return Products.objects.filter(type='cpu')
    def perform_create(self, serializer):
        serializer.save(type='cpu')

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

class MotherboardView(generics.ListCreateAPIView):
    serializer_class = MotherboardSerializer

    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        if brand:
            return Products.objects.filter(brand=brand, type='motherboard')
        else:
            return Products.objects.filter(type='motherboard')
        
    def perform_create(self, serializer):
        serializer.save(type='motherboard')

class MotherboardEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MotherboardSerializer
    queryset = Products.objects.filter(type='motherboard')

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

    def perform_create(self, serializer):
        product = serializer.validated_data['products']
        order = serializer.validated_data['orders']
        
        if product.type == 'cpu':
            # Check if the order already has a motherboard
            existing_motherboard = OrderItems.objects.filter(orders=order, products__type='motherboard').first()
            if existing_motherboard and existing_motherboard.products.socket != product.socket:
                raise ValidationError('Selected CPU is not compatible with the existing motherboard in the order.')

        if product.type == 'motherboard':
            existing_cpu = OrderItems.objects.filter(orders=order, products__type='cpu').first()
            if existing_cpu and existing_cpu.products.socket != product.socket:
                raise ValidationError('Selected motherboard is not compatible with the existing CPU in the order.')

        serializer.save()
class BrandNamesListView(generics.ListCreateAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer

class BrandNamesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer

class OrderItemEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = GetOrderItemsSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        quantity = data.get('quantity')
        if quantity is not None:
            instance.quantity = quantity

        instance.save()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data, status=status.HTTP_200_OK)