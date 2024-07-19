from django.db import models

PC_COMPONENTS = (
    ("CPU", "CPU"),
    ("GPU", "GPU"),
    ("RAM", "RAM"),
    ("MOTHERBOARD", "MOTHERBOARD"),
    ("OS", "OS"),
    ("WIFI", "WIFI"),
    ("CASE", "CASE"),
    ("COOLER", "COOLER"),
    ("SSD", "SSD"),
    ("HDD", "HDD"),
    ("POWERSUPPLY", "POWERSUPPLY"),
    ("MOUSE", "MOUSE"),
    ("MONITOR", "MONITOR"),
    ("KEYBOARD", "KEYBOARD"),
    ("HEADSET", "HEADSET"),
)

class Components(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    cpu = models.ForeignKey('CpuList', on_delete=models.SET_NULL, null=True, blank=True)
    # Add other components similarly
    total_price = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)

    def calculate_total_price(self):
        total = 0
        if self.cpu:
            total += self.cpu.price
        return total

class Orders(models.Model):
    components = models.ManyToManyField(Components)
    created_at = models.DateTimeField(auto_now_add=True)

class BrandNamesList(models.Model):
    brandName = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='cpu_pictures/', blank=True, default=None)
    type = models.CharField(default="Please choose", choices=PC_COMPONENTS, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brandName

class CpuList(models.Model):
    name = models.CharField(max_length=255)
    socket = models.CharField(max_length=255)
    numberOfCores = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(BrandNamesList, related_name='cpulist_items', default=None, on_delete=models.CASCADE)

