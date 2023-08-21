from django.urls import path

from . import views


urlpatterns = [
    path("", views.MailingEmailAddressCreateAPIView.as_view()),
    path("<uuid:pk>/", views.MailingEmailAddressDestroyAPIView.as_view()),
]
