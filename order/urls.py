from django.urls import path

from . import views


urlpatterns = [
    path("list/", views.OrderListAPIView.as_view()),
    path("checkout/", views.OrderCreateAPIView.as_view()),
    path("<uuid:pk>/", views.OrderRetrieveDestroyAPIView.as_view()),
]
