from rest_framework import serializers
from .models import *
from .config.product_config import QUANTITY_LIMITS


class CpuSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="cpu"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    socket = serializers.CharField(required=True, error_messages={
        'required': 'The socket field is required.',
        'blank': 'The socket field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "total_amount", "name", "socket", "numberOfCores", "price", "brand", "picture_cpu", "type"]
        read_only_fields = ["type"]

class OsSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="os"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "socket", "price", "brand", "type"]
        read_only_fields = ["type"]

class WifiSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="wifi"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "socket", "wirelessStandart", "picture_wifi", "price", "numberOfAntennas", "security", "brand", "type"]
        read_only_fields = ["type"]
class CaseSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="case"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "formFactor", "videCardLength", "picture_case", "price", "brand", "type"]
        read_only_fields = ["type"]
class CoolerSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="cooler"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "radiatorMaterial", "noiseLevel", "rotationalSpeed", "picture_cooler", "price", "brand", "type"]
        read_only_fields = ["type"]
class MotherboardSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="motherboard"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    socket = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    ramSlots = serializers.IntegerField(required=True, error_messages={
        'required': 'The ramSlots field is required.',
        'blank': 'The ramSlots field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "socket", "total_amount", "chipset", "formFactor", "ramSlots", "picture_motherboard", "price", "brand", "type"]
        read_only_fields = ["type"]

class GpuSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="gpu"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "coreClock", "total_amount", "boostClock", "picture_gpu", "price", "brand", "type"]
        read_only_fields = ["type"]
class SsdSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="ssd"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "readSpeed", "total_amount", "writeSpeed", "picture_ssd", "price", "brand", "type"]
class HddSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="hdd"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "readSpeed", "total_amount", "writeSpeed", "picture_hdd", "price", "brand", "type"]
        read_only_fields = ["type"]
class RamSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="ram"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "speed", "total_amount", "picture_ram", "price", "brand", "type"]
        read_only_fields = ["type"]
class PsuSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="psu"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "wattage", "total_amount", "picture_psu", "price", "brand", "type"]
        read_only_fields = ["type"]

class MouseSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="mouse"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "dpi", "total_amount", "picture_mouse", "price", "brand", "type"]
        read_only_fields = ["type"]

class MonitorSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="monitor"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "size", "resolution", "refreshRate", "total_amount", "picture_monitor", "price", "brand", "type"]
        read_only_fields = ["type"]

class KeyboardSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="keyboard"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "switches", "total_amount", "picture_keyboard", "price", "brand", "type"]
        read_only_fields = ["type"]


class HeadsetSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="headset"))
    name = serializers.CharField(required=True, error_messages={
        'required': 'The name field is required.',
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "connectionInterface", "total_amount", "picture_headset", "price", "brand", "type"]
        read_only_fields = ["type"]
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
class PostOrderItemsSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())    
    class Meta:
        model = OrderItems
        fields = ['id', 'quantity', 'products', 'orders']
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                f"The maximum quantity allowed for {type_name.upper()} is {QUANTITY_LIMITS[type_name]}."
            )
        product = self.instance.products if self.instance else Products.objects.get(id=self.initial_data['products'])
        type_name = product.type.lower()
        
        if type_name in QUANTITY_LIMITS and value > QUANTITY_LIMITS[type_name]:
            raise serializers.ValidationError(
                f"The maximum quantity allowed for {type_name.upper()} is {QUANTITY_LIMITS[type_name]}."
            )
        return value
    
class GetOrderItemsSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    subtotal_price = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderItems
        fields = ['id', 'quantity', 'subtotal_price', 'product']
        
    def get_product(self, obj):
        product = obj.products
        product_type = product.type.lower()
        serializer = self.get_serializer_for_type(product_type)
        return serializer(product).data

    def get_serializer_for_type(self, product_type):
        serializers_map = {
            'cpu': CpuSerializer,
            'gpu': GpuSerializer,
            'os': OsSerializer,
            'wifi': WifiSerializer,
            'case': CaseSerializer,
            'cooler': CoolerSerializer,
            'motherboard': MotherboardSerializer,
            'ssd': SsdSerializer,
            'hdd': HddSerializer,
            'ram': RamSerializer,
            'psu': PsuSerializer
        }
        return serializers_map.get(product_type, ProductSerializer)

    def get_subtotal_price(self, obj):
        return obj.quantity * obj.products.price
class GetOrderSerializer(serializers.ModelSerializer):
    components = GetOrderItemsSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Orders
        fields = ["id", "total_price", "components"]

    def get_total_price(self, obj):
        total = 0
        for item in obj.components.all():
            total += item.quantity * item.products.price
        return total

class PostOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["id"]
class BrandNamesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandNamesList
        fields = "__all__"
