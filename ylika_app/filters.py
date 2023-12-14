import django_filters
from .models import Proion 

class StockFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Proion
        fields = ['onoma']