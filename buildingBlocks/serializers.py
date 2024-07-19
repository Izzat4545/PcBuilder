from rest_framework import serializers
from .models import Components, Orders, BrandNamesList, CpuList


class CpuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuList
        fields = "__all__"
class ComponentsSerializer(serializers.ModelSerializer):
    cpu = CpuListSerializer(read_only=True)
    class Meta:
        model = Components
        fields = "__all__"
class OrdersSerializer(serializers.ModelSerializer):
    components = ComponentsSerializer(many=True, read_only=True)

    class Meta:
        model = Orders
        fields = '__all__'

class BrandNamesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandNamesList
        fields = "__all__"

class ComponentSelectionSerializer(serializers.Serializer):
    cpu_id = serializers.IntegerField(required=False)
    # gpu_id = serializers.IntegerField(required=False)
    # ram_id = serializers.IntegerField(required=False)
    # Add fields for other components similarly

    def create(self, validated_data):
        components_data = {
            'cpu': CpuList.objects.get(id=validated_data.get('cpu_id')) if validated_data.get('cpu_id') else None,
            # 'gpu': GpuList.objects.get(id=validated_data.get('gpu_id')) if validated_data.get('gpu_id') else None,
            # 'ram': RamList.objects.get(id=validated_data.get('ram_id')) if validated_data.get('ram_id') else None,
            # Add other components similarly
        }
        components = Components.objects.create(**components_data)
        return components
