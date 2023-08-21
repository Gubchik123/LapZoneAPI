from django_filters import rest_framework as filters

from .models import Product


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """Custom filter for CharField."""


class ProductFilter(filters.FilterSet):
    """Filter set for the Product model."""

    year = filters.RangeFilter()
    price = filters.RangeFilter()

    class Meta:
        """Meta options for the ProductFilter."""

        model = Product
        fields = ("year", "price", "brand", "category")
