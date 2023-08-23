from django.conf import settings
from django.contrib.sessions.backends.base import SessionBase

from shop.models import Product
from shop.serializers import ProductListSerializer


class Cart:
    """
    Shopping cart that stores products, their quantities and their prices.
    """

    def __init__(self, request_session: SessionBase) -> None:
        """Initializes a new cart instance."""
        self.session = request_session
        if not (cart := self.session.get(settings.CART_SESSION_ID)):
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterates over the items in the cart and yield each item dictionary.
        """
        for item in self.cart.values():
            yield item

    def add(self, product: Product, quantity: int) -> None:
        """Adds a product to the cart"""
        if (product_id := str(product.id)) not in self.cart:
            self.cart[product_id] = {
                "quantity": quantity,
                "price": product.price,
                "total_price": product.price * quantity,
                "product": ProductListSerializer(product).data,
            }
            self._save()

    def update(self, product_id: int, quantity: int) -> None:
        """Updates the cart product quantity."""
        if (product_id := str(product_id)) in self.cart:
            self.cart[product_id]["quantity"] = quantity
            self.cart[product_id]["total_price"] = (
                quantity * self.cart[product_id]["price"]
            )
            self._save()

    def remove(self, product_id: int) -> None:
        """Removes a product from the cart."""
        if (product_id := str(product_id)) in self.cart:
            del self.cart[product_id]
            self._save()

    def _save(self) -> None:
        """Saves the current state of the cart to the session."""
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
