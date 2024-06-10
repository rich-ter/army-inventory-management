# filters.py
import django_filters
from .models import Product, Shipment, ProductCategory, ProductUsage, Recipient
from django.db.models import Q
from unidecode import unidecode
from django import forms

class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_all', label='Search')

    class Meta:
        model = Product
        fields = ['name', 'category', 'usage', 'description']

    def normalize_input(self, value):
        return value.strip().lower()

    def filter_by_all(self, queryset, name, value):
        if not value:
            return queryset
        normalized_value = self.normalize_input(value)
        return queryset.filter(
            Q(name__icontains=normalized_value) |
            Q(category__name__icontains=normalized_value) |
            Q(usage__name__icontains=normalized_value) |
            Q(description__icontains=normalized_value)
        )

class ShipmentFilter(django_filters.FilterSet):
    order_number = django_filters.CharFilter(field_name='id', lookup_expr='exact', label='Order Number')
    recipient = django_filters.ModelChoiceFilter(queryset=Recipient.objects.all(), label='Recipient')
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='Από')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}), label='Έως')

    class Meta:
        model = Shipment
        fields = ['shipment_type', 'recipient', 'order_number', 'start_date', 'end_date', 'notes']


class RecipientFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_all', label='Search')

    class Meta:
        model = Recipient
        fields = []

    def normalize_input(self, value):
        return unidecode(value.strip().lower())

    def filter_by_all(self, queryset, name, value):
        if not value:
            return queryset
        normalized_value = self.normalize_input(value)
        return queryset.filter(
            Q(commanding_unit__icontains=normalized_value) |
            Q(recipient_unit__icontains=normalized_value)
        )