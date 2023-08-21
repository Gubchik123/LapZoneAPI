from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class IsOwner(BasePermission):
    """Permission to only allow owners of an object to get it."""

    def has_object_permission(
        self, request: Request, view: APIView, obj: User
    ) -> bool:
        """Returns True if the user is the owner of the fetched list."""
        user_obj = obj if isinstance(obj, User) else obj.user
        return request.user.is_authenticated and user_obj == request.user
