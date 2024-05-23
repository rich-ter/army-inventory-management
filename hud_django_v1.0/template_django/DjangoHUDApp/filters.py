# filters.py
import django_filters
from .models import Product, Shipment
from django.db.models import Q
from unidecode import unidecode

class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_all')

    class Meta:
        model = Product
        fields = ['name', 'category', 'usage', 'description']

    def filter_by_all(self, queryset, name, value):
        value = unidecode(value.lower())
        return queryset.filter(
            Q(name__icontains=value) |
            Q(category__icontains=value) |
            Q(usage__icontains=value) |
            Q(description__icontains=value)
        )

class ShipmentFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_all')

    class Meta:
        model = Shipment
        fields = ['shipment_type', 'date', 'notes']

    def filter_by_all(self, queryset, name, value):
        value = unidecode(value.lower())
        return queryset.filter(
            Q(shipment_type__icontains=value) |
            Q(date__icontains=value) |
            Q(notes__icontains=value)
        )
