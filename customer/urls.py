from django.urls import path

from . import views


urlpatterns = [
    path("<username>/", views.CustomerRetrieveUpdateDestroyAPIView.as_view()),
    path("<username>/wish-list/", views.CustomerWishListAPIView.as_view()),
]
