from rest_framework import generics
from rest_framework.response import Response

from . import serializers
from general.permissions import IsOwner
from .services import process_and_get_order_or_response


class _OrderAPIMixin:
    """Mixin for order API views."""

    permission_classes = [IsOwner]

    def get_queryset(self):
        """Returns the user orders."""
        if self.request.user.is_authenticated:
            return self.request.user.order_set.all()
        return []


class OrderCreateAPIView(generics.CreateAPIView):
    """API view for the order creation."""

    serializer_class = serializers.OrderCreateSerializer

    def create(self, request, *args, **kwargs) -> Response:
        """Creates the order and returns the response."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = process_and_get_order_or_response(request)
        headers = self.get_success_headers(serializer.data)
        return Response(order, status=201, headers=headers)


class OrderListAPIView(_OrderAPIMixin, generics.ListAPIView):
    """API view for the list of orders."""

    serializer_class = serializers.OrderListSerializer


class OrderRetrieveDestroyAPIView(
    _OrderAPIMixin, generics.RetrieveDestroyAPIView
):
    """API view for the order detail."""

    serializer_class = serializers.OrderDetailSerializer
