from django.contrib import admin
from .models import Product, Warehouse, Recipient, Shipment, ShipmentItem, Stock
from django.core.exceptions import ValidationError

class ShipmentItemInline(admin.TabularInline):
    model = ShipmentItem
    extra = 1  # Number of empty forms to display

class ShipmentAdmin(admin.ModelAdmin):
    inlines = [ShipmentItemInline,]

# Register your models with the admin site
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Recipient)
# Make sure to register Shipment with ShipmentAdmin only once
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Stock)
# admin.site.register(ProductInstance)
