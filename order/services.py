from uuid import uuid4, UUID

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.template.loader import render_to_string

from .models import Order, OrderItem
from cart.cart import Cart


def _send_email_to_customer_by_(
    email: str, order_id: UUID, request: HttpRequest
) -> None:
    """Sends a receipt email to the customer at the given email address."""
    send_mail(
        "Thank you for your order from LapZone!",
        "Your order has been received and is currently being processed.",
        settings.EMAIL_HOST_USER,
        [email],
        html_message=render_to_string(
            "order/email.html",
            {
                "email": email,
                "order_id": order_id,
            },
            request,
        ),
    )


def _get_or_create_user_with_data_from_(
    request_data: dict,
) -> tuple[User, bool]:
    """Returns a user with the data from the given OrderCreateModelForm."""
    user, was_created = User.objects.get_or_create(email=request_data["email"])
    if was_created:
        user.username = request_data["username"]
        user.set_password(request_data["password"])
    return user, was_created


def _update_user_personal_details(user: User, request_data: dict) -> None:
    """Updates the personal details such as first and last name for user
    if they are empty with the data from the given OrderCheckoutModelForm."""
    was_changed = False
    if not user.first_name:
        was_changed = True
        user.first_name = request_data["first_name"]
    if not user.last_name:
        was_changed = True
        user.last_name = request_data["last_name"]
    if was_changed:
        user.save()


def _get_or_create_user(request: HttpRequest) -> User | None:
    """Returns a user if the user is authenticated or
    creates a new user if 'is_create_profile' is True."""
    user = None

    if request.user.is_authenticated:
        user = request.user
    elif request.data["is_create_profile"] == "True":
        user, was_created = _get_or_create_user_with_data_from_(request.data)
        # if was_created:
        #     send_email_confirmation(request, user)
    if user is not None:
        _update_user_personal_details(user, request.data)
    return user


def _create_order_for_user_with_data_from_(
    cart: Cart, user: User, order_id: UUID
) -> Order:
    """
    Creates an order for the given user with the data from the given cart.
    Returns the absolute url of the created order.
    """
    order = Order.objects.create(
        id=order_id, user=user, total_price=cart.get_total_price()
    )
    for item_dict in cart:
        OrderItem.objects.create(
            order=order,
            product=item_dict["product"],
            quantity=item_dict["quantity"],
            price=item_dict["price"],
            total_price=item_dict["price"] * item_dict["quantity"],
        )
    return order


def process_and_get_order_or_response(request: HttpRequest) -> Order | dict[str, str]:
    """
    Processes an order by the given request and returns the it or response.
    """
    order_id = uuid4()
    # _send_email_to_customer_by_(
    #     request.data.get("email", None) or request.user.email,
    #     order_id,
    #     request,
    # )
    order = None
    cart = Cart(request.session)
    if (user := _get_or_create_user(request)) is not None:
        order = _create_order_for_user_with_data_from_(cart, user, order_id)
    cart.clear()
    return order or {"message": "Receipt sent to your email."}
