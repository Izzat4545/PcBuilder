from rest_framework import generics, response,status
from .models import Components, Orders, BrandNamesList, CpuList
from .serializers import ComponentsSerializer, OrdersSerializer, BrandNamesListSerializer, CpuListSerializer, ComponentSelectionSerializer

class ComponentsView(generics.ListCreateAPIView):
    queryset = Components.objects.all()
    serializer_class = ComponentsSerializer

class ComponentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Components.objects.all()
    serializer_class = ComponentsSerializer

class OrdersView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class OrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class BrandNamesListView(generics.ListCreateAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer

class BrandNamesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BrandNamesList.objects.all()
    serializer_class = BrandNamesListSerializer

class CpuListView(generics.ListCreateAPIView):
    queryset = CpuList.objects.all()
    serializer_class = CpuListSerializer

class CpuListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CpuList.objects.all()
    serializer_class = CpuListSerializer

class SelectComponentsView(generics.CreateAPIView):
    serializer_class = ComponentSelectionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        components = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return response.Response(ComponentsSerializer(components).data, status=status.HTTP_201_CREATED, headers=headers)
