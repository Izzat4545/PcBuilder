from django.contrib import admin
from .models import Products, BrandNamesList, Orders, OrderItems
from unfold.admin import ModelAdmin, TabularInline
@admin.register(BrandNamesList)
class BrandNamesListAdmin(ModelAdmin):
    list_display = ['brandName', 'type', 'created_at']
    search_fields = ['brandName', 'type']

class OrderItemsInline(TabularInline):
    model = OrderItems
    extra = 0
    tab = False
@admin.register(Orders)
class OrdersAdmin(ModelAdmin):
    list_display = ['id', 'username', 'phoneNumber', 'total_price', 'created_at']
    search_fields = ['username', 'phoneNumber']
    readonly_fields = ['total_price']
    inlines = [OrderItemsInline]


@admin.register(Products)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'type', 'price', 'brand', 'created_at']
    list_filter = ['type', 'brand']
    search_fields = ['name', 'socket', 'chipset']

    def get_fieldsets(self, request, obj=None):
        common_fields = ('Common Information', {
            'fields': ('name', 'price', 'brand', 'type')
        })

        if obj:
            if obj.type == 'cpu':
                fieldsets = [
                    common_fields,
                    ('CPU Specific', {
                        'fields': ('socket', 'numberOfCores', 'picture_cpu')
                    }),
                ]
            elif obj.type == 'gpu':
                fieldsets = [
                    common_fields,
                    ('GPU Specific', {
                        'fields': ('coreClock', 'boostClock', 'picture_gpu')
                    }),
                ]
            elif obj.type == 'os':
                fieldsets = [
                    common_fields,
                    ('OS Specific', {
                        'fields': ()
                    }),
                ]
            elif obj.type == 'wifi':
                fieldsets = [
                    common_fields,
                    ('WiFi Specific', {
                        'fields': ('wirelessStandart', 'numberOfAntennas', 'security', 'picture_wifi')
                    }),
                ]
            elif obj.type == 'case':
                fieldsets = [
                    common_fields,
                    ('Case Specific', {
                        'fields': ('formFactor', 'videCardLength', 'picture_case')
                    }),
                ]
            elif obj.type == 'cooler':
                fieldsets = [
                    common_fields,
                    ('Cooler Specific', {
                        'fields': ('radiatorMaterial', 'noiseLevel', 'rotationalSpeed', 'picture_cooler')
                    }),
                ]
            elif obj.type == 'motherboard':
                fieldsets = [
                    common_fields,
                    ('Motherboard Specific', {
                        'fields': ('socket', 'chipset', 'formFactor', 'ramSlots', 'picture_motherboard')
                    }),
                ]
            elif obj.type == 'ssd':
                fieldsets = [
                    common_fields,
                    ('SSD Specific', {
                        'fields': ('readSpeed', 'writeSpeed', 'picture_ssd')
                    }),
                ]
            elif obj.type == 'hdd':
                fieldsets = [
                    common_fields,
                    ('HDD Specific', {
                        'fields': ('readSpeed', 'writeSpeed', 'picture_hdd')
                    }),
                ]
            elif obj.type == 'ram':
                fieldsets = [
                    common_fields,
                    ('RAM Specific', {
                        'fields': ('speed', 'picture_ram')
                    }),
                ]
            elif obj.type == 'psu':
                fieldsets = [
                    common_fields,
                    ('PSU Specific', {
                        'fields': ('wattage', 'picture_psu')
                    }),
                ]
            elif obj.type == 'mouse':
                fieldsets = [
                    common_fields,
                    ('Mouse Specific', {
                        'fields': ('dpi', 'picture_mouse')
                    }),
                ]
            elif obj.type == 'monitor':
                fieldsets = [
                    common_fields,
                    ('Monitor Specific', {
                        'fields': ('size', 'resolution', 'refreshRate', 'picture_monitor')
                    }),
                ]
            elif obj.type == 'keyboard':
                fieldsets = [
                    common_fields,
                    ('Keyboard Specific', {
                        'fields': ('switches', 'picture_keyboard')
                    }),
                ]
            elif obj.type == 'headset':
                fieldsets = [
                    common_fields,
                    ('Headset Specific', {
                        'fields': ('connectionInterface', 'picture_headset')
                    }),
                ]
            else:
                fieldsets = [common_fields]
        else:
            fieldsets = [common_fields]
        
        return fieldsets
