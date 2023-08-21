from rest_framework import serializers
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for user model."""

    orders_count = serializers.SerializerMethodField(
        method_name="get_order_count"
    )
    likes_count = serializers.SerializerMethodField(
        method_name="get_likes_count"
    )

    def get_order_count(self, user: User) -> int:
        """Returns the number of orders placed by the user."""
        return user.order_set.count()

    def get_likes_count(self, user: User) -> int:
        """Returns the number of products liked by the user."""
        return user.like_set.count()

    class Meta:
        """Meta options for the UserSerializer."""

        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "orders_count",
            "likes_count",
        )
        read_only_fields = (
            "id",
            "username",
            "email",
            "orders_count",
            "likes_count",
        )
