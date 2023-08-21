from rest_framework import generics
from rest_framework.request import Request
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import User


class IsOwnerOrReadOnly(BasePermission):
    """Permission to only allow owners of an object to edit it."""

    def has_object_permission(
        self,
        request: Request,
        view: generics.RetrieveUpdateDestroyAPIView,
        obj: User,
    ) -> bool:
        """Returns True if the request method is safe
        or the user is the owner of the fetched profile."""
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
