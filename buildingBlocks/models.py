from django.db import models

# Create your models here.
class Orders(models.Model):
    orders = models.JSONField()

class PcComponents(models.Model):
    components = models.JSONField()
    isFinished = models.BooleanField(default=False)
    totalPrice = models.IntegerField(default=0)

class CpuBrandNamesList(models.Model):
    brandName = models.CharField(max_length=255)
    cpulist = models.JSONField()
    picture = models.ImageField(upload_to='cpu_pictures/')
    created_at = models.DateTimeField(auto_now_add=True)

class CpuList(models.Model):
    name = models.CharField(max_length=255)
    isSelected = models.BooleanField(default=False)
    socket = models.CharField(max_length=255)
    numberOfCores = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    cpulist = models.ForeignKey(CpuBrandNamesList, related_name='cpulist_items', on_delete=models.CASCADE)

class CPU(models.Model):
    brandNames = models.JSONField()
    pc_components = models.ForeignKey(PcComponents, related_name='cpu_components', on_delete=models.CASCADE)
