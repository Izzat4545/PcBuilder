from rest_framework import serializers
from .models import *
import logging

logger = logging.getLogger(__name__)


class CpuSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="cpu"))
    class Meta:
        model = Products
        fields = ["id", "total_amount", "name", "socket", "numberOfCores", "price", "brand", "picture_cpu", "type"]

class OsSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="os"))
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "socket", "price" "brand", "type"]

class WifiSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="wifi"))
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "socket", "wirelessStandart", "picture_wifi" "price", "numberOfAntennas", "security", "brand", "type"]

class CaseSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="case"))
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "formfactor", "videCardLength", "picture_case", "price", "brand", "type"]

class CoolerSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="cooler"))
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "radiatorMaterial", "noiseLevel", "rotationalSpeed", "picture_cooler", "price", "brand", "type"]

class MotherboardSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="motherboard"))
    class Meta:
        model = Products
        fields = ["id", "name", "socket", "total_amount", "chipset", "formFactor", "picture_motherboard", "price", "brand", "type"]

class GpuSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="gpu"))
    class Meta:
        model = Products
        fields = ["id", "name", "coreClock", "total_amount", "boostClock", "picture_gpu", "price", "brand", "type"]
        read_only_fields = ["type"]
class SsdSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="ssd"))
    class Meta:
        model = Products
        fields = ["id", "name", "readspeed", "total_amount", "writeSpeed", "picture_ssd", "price", "brand", "type"]
class HddSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="hdd"))
    class Meta:
        model = Products
        fields = ["id", "name", "readspeed", "total_amount", "writeSpeed", "picture_hdd", "price", "brand", "type"]

class RamSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="ram"))
    class Meta:
        model = Products
        fields = ["id", "name", "speed", "total_amount", "picture_ram", "price", "brand", "type"]

class PsuSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="psu"))
    class Meta:
        model = Products
        fields = ["id", "name", "wattage", "total_amount", "picture_psu", "price", "brand", "type"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
class PostOrderItemsSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    class Meta:
        model = OrderItems
        fields = ['id', 'quantity', 'products', 'orders']
    
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
