from rest_framework import generics, response,status
from .models import  Orders, BrandNamesList, CpuList
from .serializers import OrdersSerializer, BrandNamesListSerializer, CpuListSerializer, ComponentSelectionSerializer


class OrdersView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class OrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class CreateOrderView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def create(self, request, *args, **kwargs):
        order = Orders.objects.create()
        return response.Response({'order_id': order.id}, status=status.HTTP_201_CREATED)


class BrandNamesListView(generics.ListCreateAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer

class BrandNamesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer

class CpuListView(generics.ListCreateAPIView):
    queryset = CpuList.objects.all()
    serializer_class = CpuListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        brand_id = self.request.query_params.get('brand_id', None)

        if brand_id:
            queryset = queryset.filter(brand=brand_id)

        return queryset

class CpuListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CpuList.objects.all()
    serializer_class = CpuListSerializer

class SelectComponentsView(generics.CreateAPIView):
    serializer_class = ComponentSelectionSerializer

    def create(self, request, *args, **kwargs):
        # Deserialize and validate input
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the order with updated components
        order = serializer.save()
        
        # Return the updated order details
        return response.Response(OrdersSerializer(order).data, status=status.HTTP_200_OK)

