from django.db import models
from .config import product_config

class BrandNamesList(models.Model):
    brandName = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='brand/', blank=True, default=None)
    type = models.CharField(default="Please choose", choices=product_config.PC_COMPONENTS, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brandName

class Products(models.Model):
    total_amount = models.IntegerField(default=1)
    name = models.CharField(max_length=255)
    socket = models.CharField(max_length=255)
    numberOfCores = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(default=0)
    type = models.CharField(default="Please choose", choices=product_config.PC_COMPONENTS, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    picture_cpu = models.ImageField(upload_to='images/cpu/', blank=True, default=None)
    brand = models.ForeignKey(BrandNamesList, default=None, on_delete=models.PROTECT)
    wirelessStandart = models.CharField(max_length=50, blank=True, null=True)
    numberOfAntennas = models.IntegerField(blank=True, null=True)
    security = models.CharField(max_length=50, blank=True, null=True)
    picture_wifi = models.ImageField(upload_to='images/wifi/', blank=True, default=None)
    formFactor = models.CharField(max_length=50, blank=True, null=True)
    videCardLength = models.CharField(max_length=50, blank=True, null=True)
    picture_case = models.ImageField(upload_to='images/cases/', blank=True, default=None)
    radiatorMaterial = models.CharField(max_length=50, blank=True, null=True)
    rotationalSpeed = models.IntegerField(blank=True, null=True)
    noiseLevel = models.CharField(max_length=50, blank=True, null=True)
    picture_cooler = models.ImageField(upload_to='images/cooler/', blank=True, default=None)
    chipset = models.CharField(max_length=50, blank=True, null=True)
    picture_motherboard = models.ImageField(upload_to='images/motherboard/', blank=True, default=None)
    coreClock = models.CharField(max_length=50, blank=True, null=True)
    boostClock = models.CharField(max_length=50, blank=True, null=True)
    picture_gpu = models.ImageField(upload_to='images/gpu/', blank=True, default=None)
    readSpeed = models.CharField(max_length=50, blank=True, null=True)
    writeSpeed = models.CharField(max_length=50, blank=True, null=True)
    picture_ssd = models.ImageField(upload_to='images/ssd/', blank=True, default=None)
    speed = models.CharField(max_length=50, blank=True, null=True)
    picture_ram = models.ImageField(upload_to='images/ram/', blank=True, default=None)
    picture_hdd = models.ImageField(upload_to='images/hdd/', blank=True, default=None)
    wattage = models.CharField(max_length=50, blank=True, null=True)
    ramSlots = models.IntegerField(default=1, blank=True, null=True)
    picture_psu = models.ImageField(upload_to='images/psu/', blank=True, default=None)
    dpi = models.CharField(max_length=50, blank=True, null=True)
    picture_mouse = models.ImageField(upload_to='images/mouse/', blank=True, default=None)
    size = models.CharField(max_length=50, blank=True, null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    refreshRate = models.CharField(max_length=50, blank=True, null=True)
    picture_monitor = models.ImageField(upload_to='images/monitor/', blank=True, default=None)
    switches = models.CharField(max_length=50, blank=True, null=True)
    picture_keyboard = models.ImageField(upload_to='images/keyboard/', blank=True, default=None)
    connectionInterface = models.CharField(max_length=50, blank=True, null=True)
    picture_headset = models.ImageField(upload_to='images/headset/', blank=True, default=None)

    def __str__(self):
        return "{}".format(self.name)
class Orders(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    phoneNumber = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.id)

class OrderItems(models.Model):
    orderId = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="components", null=True, blank=True)
    products = models.ForeignKey(Products, on_delete=models.PROTECT, related_name="orderItems", null=True, blank=True)
    quantity = models.IntegerField(default=1)

