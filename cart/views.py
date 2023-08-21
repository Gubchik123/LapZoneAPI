from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .cart import Cart
from . import services
from shop.serializers import ProductListSerializer


class CartAPIView(APIView):
    """API view for the session-based Cart."""

    def get(self, request: Request) -> Response:
        """Returns all the cart products."""
        cart_items = []
        for item in Cart(request.session):
            item["product"] = ProductListSerializer(item["product"]).data
            cart_items.append(item)
        return Response(cart_items)

    def post(self, request: Request) -> Response:
        """Adds a product to cart and returns a response."""
        return Response(services.add_product_to_cart_and_get_response(request))

    def put(self, request: Request) -> Response:
        """Updates a cart product and returns a response."""
        return Response(services.update_cart_product_and_get_response(request))

    def delete(self, request: Request) -> Response:
        """Removes a product from cart and returns a response."""
        return Response(
            services.remove_product_from_cart_and_get_response(request)
        )
