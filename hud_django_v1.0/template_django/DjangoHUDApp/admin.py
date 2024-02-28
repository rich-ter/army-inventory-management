from django.contrib import admin

# Register your models here.
# admin.py
from .models import Product, Warehouse

admin.site.register(Product)
admin.site.register(Warehouse)
