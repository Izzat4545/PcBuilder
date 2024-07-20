from rest_framework import serializers
from .models import Orders, BrandNamesList, CpuList

class CpuListSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(
        queryset=BrandNamesList.objects.filter(type="CPU")
    )
    class Meta:
        model = CpuList
        fields = "__all__"
        read_only_fields= ["type"]

class OrdersSerializer(serializers.ModelSerializer):
    cpu = CpuListSerializer(read_only=True, many=True)
    total_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"

class BrandNamesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandNamesList
        fields = "__all__"

class ComponentSelectionSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(required=True)
    cpu_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        order = Orders.objects.get(id=validated_data['order_id'])
        if validated_data.get('cpu_id'):
            cpu_instance = CpuList.objects.get(id=validated_data['cpu_id'])
            order.cpu.add(cpu_instance)
        
        order.save()
        return order

