from rest_framework import serializers
from django.contrib.auth.models import User

from shop.models import Product
from .models import OrderItem, Order


class _MyUserSerializer(serializers.ModelSerializer):
    """Serializer for the user."""

    class Meta:
        """Meta options for the _UserSerializer."""

        model = User
        fields = ["username", "email", "password"]


class OrderCreateSerializer(serializers.ModelSerializer):
    """Serializer for order creation."""

    user = _MyUserSerializer()

    class Meta:
        """Meta options for the OrderCreateSerializer."""

        model = Order
        fields = ["user", "total_price"]
        read_only_fields = ["id", "created"]


class OrderListSerializer(serializers.ModelSerializer):
    """Serializer for the list of orders."""

    class Meta:
        """Meta options for the OrderListSerializer."""

        model = Order
        exclude = ["user"]


class _ProductDetailSerializer(serializers.ModelSerializer):
    """Serializer for product (order item) detail."""

    class Meta:
        """Meta options for the _ProductDetailSerializer."""

        model = Product
        fields = ("id", "name", "slug", "image")


class _OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for the order item."""

    product = serializers.SerializerMethodField(method_name="get_product")

    def get_product(self, order_item: OrderItem) -> str:
        """Returns the product name."""
        return _ProductDetailSerializer(order_item.product).data

    class Meta:
        """Meta options for the OrderItemSerializer."""

        model = OrderItem
        exclude = ["order"]


class OrderDetailSerializer(serializers.ModelSerializer):
    """Serializer for the order detail."""

    order_items = serializers.SerializerMethodField(
        method_name="get_order_items"
    )

    def get_order_items(self, order: Order) -> list[dict]:
        """Returns the order items."""
        return _OrderItemSerializer(order.orderitem_set.all(), many=True).data

    class Meta(OrderListSerializer.Meta):
        """Meta options for the OrderDetailSerializer."""
