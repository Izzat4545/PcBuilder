from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import BrandNamesList, Products

@receiver(post_delete, sender=BrandNamesList)
def delete_brand_picture(sender, instance, **kwargs):
    if instance.picture:
        instance.picture.delete(save=False)

@receiver(post_delete, sender=Products)
def delete_product_images(sender, instance, **kwargs):
    if instance.picture_cpu:
        instance.picture_cpu.delete(save=False)
    if instance.picture_wifi:
        instance.picture_wifi.delete(save=False)
    if instance.picture_case:
        instance.picture_case.delete(save=False)
    if instance.picture_cooler:
        instance.picture_cooler.delete(save=False)
    if instance.picture_motherboard:
        instance.picture_motherboard.delete(save=False)
    if instance.picture_gpu:
        instance.picture_gpu.delete(save=False)
    if instance.picture_ssd:
        instance.picture_ssd.delete(save=False)
    if instance.picture_ram:
        instance.picture_ram.delete(save=False)
    if instance.picture_hdd:
        instance.picture_hdd.delete(save=False)
    if instance.picture_psu:
        instance.picture_psu.delete(save=False)
    if instance.picture_mouse:
        instance.picture_mouse.delete(save=False)
    if instance.picture_monitor:
        instance.picture_monitor.delete(save=False)
    if instance.picture_keyboard:
        instance.picture_keyboard.delete(save=False)
    if instance.picture_headset:
        instance.picture_headset.delete(save=False)
