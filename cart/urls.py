from django.urls import path

from . import views


urlpatterns = [path("", views.CartAPIView.as_view())]
