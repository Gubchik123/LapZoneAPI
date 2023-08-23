import logging

from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from .cart import Cart
from shop.models import Product


logger = logging.getLogger(__name__)


def _get_product_id_and_quantity_from_(
    request_data: dict, prefix: str
) -> tuple[int, int] | str:
    """
    Extracts product ID and quantity from request data and returns it or error tuple.
    """
    product_id = quantity = None
    try:
        product_id = int(request_data["product_id"])
        quantity = int(request_data["quantity"])
        return (product_id, quantity)
    except (KeyError, ValueError, TypeError):
        logger.error(f"cart product {prefix}: {product_id=}, {quantity=}")
        return (settings.ERROR_MESSAGE, None)


def _process_cart_product(request: HttpRequest, action: str) -> dict[str, str]:
    """Processes a cart product based on action and returns a response."""
    product_id, quantity = _get_product_id_and_quantity_from_(
        request.data, prefix=action
    )
    if isinstance(product_id, str):
        return {"detail": product_id}  # product_id is an error message

    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request.session)
    cart.add(product, quantity) if action == "adding" else cart.update(
        product_id, quantity
    )
    return list(cart)


def add_product_to_cart_and_get_response(
    request: HttpRequest,
) -> dict[str, str]:
    """Adds a product to cart and returns a response."""
    return _process_cart_product(request, action="adding")


def update_cart_product_and_get_response(
    request: HttpRequest,
) -> dict[str, str]:
    """Updates a cart product and returns a response."""
    return _process_cart_product(request, action="updating")


def remove_product_from_cart_and_get_response(
    request: HttpRequest,
) -> dict[str, str]:
    """Removes a product from cart and returns a response."""
    product_id = None
    try:
        product_id = int(request.data["product_id"])
    except (KeyError, ValueError, TypeError):
        logger.error(f"cart product removing: {product_id=}")
        return {"detail": settings.ERROR_MESSAGE}
    get_object_or_404(Product, id=product_id)
    cart = Cart(request.session)
    cart.remove(product_id)
    return list(cart)
