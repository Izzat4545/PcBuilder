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
    type = models.CharField(max_length=50, default="CPU", auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(BrandNamesList, related_name='cpulist_items', default=None, on_delete=models.CASCADE)


class Orders(models.Model):
    cpu = models.ManyToManyField(CpuList, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.total_price = self.calculate_total_price()
        super().save(update_fields=['total_price'])
# will be changed in the future
    def calculate_total_price(self):
        total = 0
        for cpu in self.cpu.all():
            total += cpu.price
        return total

    def __str__(self):
        return f"Order {self.id} Total Price {self.total_price}"

    def __str__(self):
        return f"Order {self.id} Total Price {self.total_price}"
