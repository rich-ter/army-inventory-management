from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    stock_by_warehouse = serializers.SerializerMethodField()
    total_stock = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'serial_number', 'category', 'usage', 'description']
    
    def get_stock_by_warehouse(self, obj):
        return obj.stock_by_warehouse()
    
    def get_total_stock(self, obj):
        return obj.total_stock()
