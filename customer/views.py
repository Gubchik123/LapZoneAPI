from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import CustomerSerializer
from .permissions import IsOwnerOrReadOnly
from general.permissions import IsOwner
from shop.serializers import ProductListSerializer
from shop.models import Product


class CustomerRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    """Generic API view for retrieve, update and destroy user."""

    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CustomerWishListAPIView(generics.ListAPIView):
    """Generic API view for list of user's liked products."""

    permission_classes = (IsOwner,)
    serializer_class = ProductListSerializer

    def get_queryset(self):
        """Returns the list of user's liked products."""
        liked_product_ids = self.request.user.like_set.values_list(
            "product_id", flat=True
        )
        return Product.objects.filter(pk__in=liked_product_ids)
