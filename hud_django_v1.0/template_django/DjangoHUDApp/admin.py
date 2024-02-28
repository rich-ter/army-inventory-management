from django.contrib import admin

# Register your models here.
# admin.py
from .models import Product

admin.site.register(Product)
