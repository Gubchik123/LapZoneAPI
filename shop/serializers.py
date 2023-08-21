from rest_framework import serializers

from . import models


class CarouselImageListSerializer(serializers.ModelSerializer):
    """Serializer for carousel image list."""

    product_slug = serializers.SlugRelatedField(
        "slug", read_only=True, source="product"
    )

    class Meta:
        """Meta options for the CarouselImageListSerializer."""

        model = models.CarouselImage
        fields = ("image", "product_slug")


class _NameAndSlugSerializer(serializers.ModelSerializer):
    """Serializer for name and slug fields."""

    class Meta:
        """Meta options for the _NameAndSlugSerializer."""

        fields = ("name", "slug")


class BrandListSerializer(serializers.ModelSerializer):
    """Serializer for brand list."""

    class Meta(_NameAndSlugSerializer.Meta):
        """Meta options for the BrandListSerializer."""

        model = models.Brand


class CategoryListSerializer(serializers.ModelSerializer):
    """Serializer for category list."""

    class Meta(_NameAndSlugSerializer.Meta):
        """Meta options for the CategoryListSerializer."""

        model = models.Category


class ProductListSerializer(serializers.ModelSerializer):
    """Serializer for product list."""

    class Meta:
        """Meta options for the ProductListSerializer."""

        model = models.Product
        fields = ("name", "slug", "price", "image")


class _RecursiveSerializer(serializers.Serializer):
    """Serializer for recursive displaying."""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class _FilterReviewSerializer(serializers.ListSerializer):
    """Serializer for filtering reviews."""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class _ReviewDetailSerializer(serializers.ModelSerializer):
    """Serializer for Review detail."""

    children = _RecursiveSerializer(many=True)

    class Meta:
        """Meta options for the ReviewDetailSerializer."""

        model = models.Review
        exclude = ("product", "parent")
        list_serializer_class = _FilterReviewSerializer


class _LikeDetailSerializer(serializers.ModelSerializer):
    """Serializer for Like detail."""

    class Meta:
        """Meta options for the LikeDetailSerializer."""

        model = models.Like
        exclude = ("product",)


class ProductDetailSerializer(serializers.ModelSerializer):
    """Serializer for product detail."""

    brand = serializers.SlugRelatedField(slug_field="name", read_only=True)
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    reviews = _ReviewDetailSerializer(many=True)
    likes = _LikeDetailSerializer(many=True)

    class Meta:
        """Meta options for the ProductDetailSerializer."""

        model = models.Product
        fields = "__all__"


class ProductReviewCreateSerializer(serializers.ModelSerializer):
    """Serializer for product review create."""

    class Meta:
        """Meta options for the ProductReviewCreateSerializer."""

        model = models.Review
        fields = ("name", "body", "parent", "product")


class ProductLikeSerializer(serializers.ModelSerializer):
    """Serializer for product like create and destroy."""

    def create(self, validated_data: dict) -> models.Like:
        """Gets or creates a like and returns it."""
        like, _ = models.Like.objects.get_or_create(
            product=validated_data["product"],
            user_id=validated_data["user_id"],
        )
        return like

    class Meta:
        """Meta options for the ProductLikeCreateDestroySerializer."""

        model = models.Like
        fields = ("product",)
