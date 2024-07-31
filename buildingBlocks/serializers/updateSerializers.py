from rest_framework import serializers
from buildingBlocks.models import *
from ..config.product_config import QUANTITY_LIMITS

class CpuEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandNamesList.objects.filter(type="cpu"), required=False)
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    socket = serializers.CharField(required=False, error_messages={
        'blank': 'The socket field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "total_amount", "name", "socket", "numberOfCores", "price", "brand", "picture_cpu", "type"]
        read_only_fields = ["type"]

class GpuEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="gpu"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "coreClock", "total_amount", "boostClock", "picture_gpu", "price", "brand", "type"]
        read_only_fields = ["type"]

class MotherboardEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="motherboard"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    socket = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    ramSlots = serializers.IntegerField(required=False, error_messages={
        'blank': 'The ramSlots field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "socket", "total_amount", "chipset", "formFactor", "ramSlots", "picture_motherboard", "price", "brand", "type"]
        read_only_fields = ["type"]

class OsEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="os"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "price", "brand", "type"]
        read_only_fields = ["type"]

class WifiEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="wifi"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "wirelessStandart", "picture_wifi", "price", "numberOfAntennas", "security", "brand", "type"]
        read_only_fields = ["type"]

class CaseEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="case"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "formFactor", "videCardLength", "picture_case", "price", "brand", "type"]
        read_only_fields = ["type"]

class CoolerEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="cooler"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "total_amount", "radiatorMaterial", "noiseLevel", "rotationalSpeed", "picture_cooler", "price", "brand", "type"]
        read_only_fields = ["type"]

class SsdEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="ssd"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "readSpeed", "total_amount", "writeSpeed", "picture_ssd", "price", "brand", "type"]
        read_only_fields = ["type"]


class HddEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="hdd"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "readSpeed", "total_amount", "writeSpeed", "picture_hdd", "price", "brand", "type"]
        read_only_fields = ["type"]

class RamEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="ram"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "speed", "total_amount", "picture_ram", "price", "brand", "type"]
        read_only_fields = ["type"]
class PsuEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="psu"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "wattage", "total_amount", "picture_psu", "price", "brand", "type"]
        read_only_fields = ["type"]

class MouseEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False,queryset=BrandNamesList.objects.filter(type="mouse"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "dpi", "total_amount", "picture_mouse", "price", "brand", "type"]
        read_only_fields = ["type"]

class MonitorEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="monitor"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "size", "resolution", "refreshRate", "total_amount", "picture_monitor", "price", "brand", "type"]
        read_only_fields = ["type"]

class KeyboardEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False,queryset=BrandNamesList.objects.filter(type="keyboard"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "switches", "total_amount", "picture_keyboard", "price", "brand", "type"]
        read_only_fields = ["type"]


class HeadsetEditSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(required=False, queryset=BrandNamesList.objects.filter(type="headset"))
    name = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = Products
        fields = ["id", "name", "connectionInterface", "total_amount", "picture_headset", "price", "brand", "type"]
        read_only_fields = ["type"]


class BrandNamesEditListSerializer(serializers.ModelSerializer):
    brandName = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    type = serializers.CharField(required=False, error_messages={
        'blank': 'The name field cannot be blank.'
    })
    class Meta:
        model = BrandNamesList
        fields = ["brandName", "type"]


class EditOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['username', 'phoneNumber']