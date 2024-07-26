from rest_framework import generics, response,status,permissions
from .models import  *
from .serializers import *
from .customPermission import IsAdminOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication

class CpuView(generics.ListCreateAPIView):
    serializer_class = CpuSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        if brand:
            return Products.objects.filter(brand=brand, type='cpu')
        else:
            return Products.objects.filter(type='cpu')
    def perform_create(self, serializer):
        serializer.save(type='cpu')

class CpuViewEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.filter(type='cpu')
    serializer_class = CpuSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class GpuView(generics.ListCreateAPIView):
    serializer_class = GpuSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

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
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
class MotherboardView(generics.ListCreateAPIView):
    serializer_class = MotherboardSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

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
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class OsView(generics.ListCreateAPIView):
    serializer_class = OsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        if brand:
            return Products.objects.filter(brand=brand, type='os')
        else:
            return Products.objects.filter(type='os')
        
    def perform_create(self, serializer):
        serializer.save(type='os')

class OsEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OsSerializer
    queryset = Products.objects.filter(type='os')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class WifiView(generics.ListCreateAPIView):
    serializer_class = WifiSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('wifi')
        if brand:
            return Products.objects.filter(brand=brand, type='wifi')
        else:
            return Products.objects.filter(type='wifi')
        
    def perform_create(self, serializer):
        serializer.save(type='wifi')

class WifiEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WifiSerializer
    queryset = Products.objects.filter(type='wifi')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class CaseView(generics.ListCreateAPIView):
    serializer_class = CaseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('case')
        if brand:
            return Products.objects.filter(brand=brand, type='case')
        else:
            return Products.objects.filter(type='case')
        
    def perform_create(self, serializer):
        serializer.save(type='case')

class CaseEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CaseSerializer
    queryset = Products.objects.filter(type='case')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class CoolerView(generics.ListCreateAPIView):
    serializer_class = CoolerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('cooler')
        if brand:
            return Products.objects.filter(brand=brand, type='cooler')
        else:
            return Products.objects.filter(type='cooler')
        
    def perform_create(self, serializer):
        serializer.save(type='case')

class CoolerEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoolerSerializer
    queryset = Products.objects.filter(type='cooler')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class SsdView(generics.ListCreateAPIView):
    serializer_class = SsdSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('ssd')
        if brand:
            return Products.objects.filter(brand=brand, type='ssd')
        else:
            return Products.objects.filter(type='ssd')
        
    def perform_create(self, serializer):
        serializer.save(type='ssd')

class SsdEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SsdSerializer
    queryset = Products.objects.filter(type='ssd')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class HddView(generics.ListCreateAPIView):
    serializer_class = HddSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('hdd')
        if brand:
            return Products.objects.filter(brand=brand, type='hdd')
        else:
            return Products.objects.filter(type='hdd')
        
    def perform_create(self, serializer):
        serializer.save(type='ssd')

class HddEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HddSerializer
    queryset = Products.objects.filter(type='hdd')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class RamView(generics.ListCreateAPIView):
    serializer_class = RamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('ram')
        if brand:
            return Products.objects.filter(brand=brand, type='ram')
        else:
            return Products.objects.filter(type='ram')
        
    def perform_create(self, serializer):
        serializer.save(type='ram')

class RamEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RamSerializer
    queryset = Products.objects.filter(type='ram')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class PsuView(generics.ListCreateAPIView):
    serializer_class = PsuSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('psu')
        if brand:
            return Products.objects.filter(brand=brand, type='psu')
        else:
            return Products.objects.filter(type='psu')
        
    def perform_create(self, serializer):
        serializer.save(type='psu')

class PsuEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PsuSerializer
    queryset = Products.objects.filter(type='psu')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class MouseView(generics.ListCreateAPIView):
    serializer_class = MouseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('mouse')
        if brand:
            return Products.objects.filter(brand=brand, type='mouse')
        else:
            return Products.objects.filter(type='mouse')
        
    def perform_create(self, serializer):
        serializer.save(type='mouse')

class MouseEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MouseSerializer
    queryset = Products.objects.filter(type='mouse')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class MonitorView(generics.ListCreateAPIView):
    serializer_class = MonitorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('monitor')
        if brand:
            return Products.objects.filter(brand=brand, type='monitor')
        else:
            return Products.objects.filter(type='monitor')
        
    def perform_create(self, serializer):
        serializer.save(type='monitor')

class MonitorEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MonitorSerializer
    queryset = Products.objects.filter(type='monitor')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
class KeyboardView(generics.ListCreateAPIView):
    serializer_class = KeyboardSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('keyboard')
        if brand:
            return Products.objects.filter(brand=brand, type='keyboard')
        else:
            return Products.objects.filter(type='keyboard')
        
    def perform_create(self, serializer):
        serializer.save(type='keyboard')

class KeyboardEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KeyboardSerializer
    queryset = Products.objects.filter(type='keyboard')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class HeadsetView(generics.ListCreateAPIView):
    serializer_class = HeadsetSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        brand = self.request.query_params.get('headset')
        if brand:
            return Products.objects.filter(brand=brand, type='headset')
        else:
            return Products.objects.filter(type='headset')
        
    def perform_create(self, serializer):
        serializer.save(type='keyboard')

class HeadsetEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HeadsetSerializer
    queryset = Products.objects.filter(type='headset')
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
class OrderAdd(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = PostOrderSerializer

class OrderView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = GetOrderSerializer

class OrderEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = GetOrderSerializer

class BrandNamesListView(generics.ListCreateAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class BrandNamesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

class OrderItemsCreate(generics.CreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = PostOrderItemsSerializer

    def perform_create(self, serializer):
        product = serializer.validated_data['products']
        order = serializer.validated_data['orders']
        
        if product.type == 'cpu':
            existing_motherboard = OrderItems.objects.filter(orders=order, products__type='motherboard').first()
            if existing_motherboard and existing_motherboard.products.socket != product.socket:
                raise ValidationError('Selected CPU is not compatible with the existing motherboard in the order.')

        if product.type == 'motherboard':
            existing_cpu = OrderItems.objects.filter(orders=order, products__type='cpu').first()
            if existing_cpu and existing_cpu.products.socket != product.socket:
                raise ValidationError('Selected motherboard is not compatible with the existing CPU in the order.')

        serializer.save()
class OrderItemEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = GetOrderItemsSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        quantity = int(data.get('quantity'))
        if quantity is not None:
            if quantity <= 0:
                raise ValidationError("Quantity must be greater than zero.")
            
            product = instance.products
            type_name = product.type.lower()
            
            if type_name in QUANTITY_LIMITS and quantity > QUANTITY_LIMITS[type_name]:
                raise ValidationError(f"The maximum quantity allowed for {type_name.upper()} is {QUANTITY_LIMITS[type_name]}.")
            
            instance.quantity = quantity
            instance.save()

        serializer = self.get_serializer(instance)
        return response.Response(serializer.data, status=status.HTTP_200_OK)