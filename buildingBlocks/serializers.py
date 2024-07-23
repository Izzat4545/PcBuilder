from rest_framework import serializers
from .models import Orders, BrandNamesList, CpuList, OrderCpu

class CpuListSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="CPU"))

    class Meta:
        model = CpuList
        fields = "__all__"
        read_only_fields = ["type"]

class OrderCpuSerializer(serializers.ModelSerializer):
    cpu = CpuListSerializer()

    class Meta:
        model = OrderCpu
        fields = ['cpu', 'amount']

class OrdersSerializer(serializers.ModelSerializer):
    cpu_selections = OrderCpuSerializer(source='ordercpu_set', many=True, read_only=True)
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
    amount = serializers.IntegerField(required=False, default=1)

    def create(self, validated_data):
        order = Orders.objects.get(id=validated_data['order_id'])
        if validated_data.get('cpu_id'):
            cpu_instance = CpuList.objects.get(id=validated_data['cpu_id'])
            OrderCpu.objects.create(order=order, cpu=cpu_instance, amount=validated_data.get('amount', 1))
        order.save()
        return order
