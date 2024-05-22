# filters.py
import django_filters
from .models import Product, Shipment

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    usage = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'category', 'usage', 'description']

class ShipmentFilter(django_filters.FilterSet):
    shipment_type = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.DateFilter()
    notes = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Shipment
        fields = ['shipment_type', 'date', 'notes']
