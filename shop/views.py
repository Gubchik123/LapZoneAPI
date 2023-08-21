from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from . import services
from . import serializers
from .filters import ProductFilter


class CarouselImageListAPIView(generics.ListAPIView):
    """Generic list API view for getting all carousel images."""

    queryset = services.get_all_carousel_images()
    serializer_class = serializers.CarouselImageListSerializer


class RecentlyAddedProductListAPIView(generics.ListAPIView):
    """Generic list API view for getting recently added products."""

    queryset = services.get_recently_added_products(5)
    serializer_class = serializers.ProductListSerializer


class BrandListAPIView(generics.ListAPIView):
    """Generic list API view for getting all brands."""

    queryset = services.get_all_brands()
    serializer_class = serializers.BrandListSerializer


class CategoryListAPIView(generics.ListAPIView):
    """Generic list API view for getting all categories."""

    queryset = services.get_all_categories()
    serializer_class = serializers.CategoryListSerializer


class _ProductListAPIMixin(generics.ListAPIView):
    """Mixin for getting all products."""

    filterset_class = ProductFilter
    filter_backends = (DjangoFilterBackend,)
    serializer_class = serializers.ProductListSerializer

    def get_queryset(self):
        """Returns queryset with all products or ordered products."""
        order_by: str | None = self.request.query_params.get("orderby", None)
        order_dir: str | None = self.request.query_params.get("orderdir", None)

        if services.are_ordering_parameters_valid(order_by, order_dir):
            order_symbol = services.get_order_symbol_by_(order_dir)
            return models.Product.objects.order_by(order_symbol + order_by)
        return models.Product.objects.all()


class ProductListAPIView(_ProductListAPIMixin):
    """Generic list API view for getting all products."""


class ProductByBrandListAPIView(_ProductListAPIMixin):
    """Generic list API view for getting all products by brand."""

    def get_queryset(self):
        """Returns queryset with products filtered by brand slug."""
        products = super().get_queryset()
        return services.get_products_filtered_by_brand_(
            self.kwargs["slug"], products
        )


class ProductByCategoryListAPIView(_ProductListAPIMixin):
    """Generic list API view for getting all products by category."""

    def get_queryset(self):
        """Returns queryset with products filtered by category slug."""
        products = super().get_queryset()
        return services.get_products_filtered_by_category_(
            self.kwargs["slug"], products
        )


class ProductSearchListAPIView(_ProductListAPIMixin):
    """Generic list API view for searching products."""

    def get_queryset(self):
        """Returns queryset with products filtered by user search input."""
        products = super().get_queryset()
        return services.get_products_that_contains_(
            self.request.query_params["q"], products
        )


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Generic retrieve API view for getting product by slug."""

    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class ProductReviewCreateAPIView(generics.CreateAPIView):
    """Generic create API view for creating product review."""

    serializer_class = serializers.ProductReviewCreateSerializer


class _ProductLikeAPIMixin:
    """Mixin for general product like API views."""

    queryset = models.Like.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ProductLikeSerializer


class ProductLikeCreateAPIView(_ProductLikeAPIMixin, generics.CreateAPIView):
    """Generic create API view for creating product like."""

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class ProductLikeDestroyAPIView(_ProductLikeAPIMixin, generics.DestroyAPIView):
    """Generic destroy API view for deleting product like."""
