from rest_framework import generics

from .models import MailingEmailAddress
from .serializers import MailingEmailAddressSerializer


class MailingEmailAddressCreateAPIView(generics.CreateAPIView):
    """Generic create API view for the MailingEmailAddress model."""

    serializer_class = MailingEmailAddressSerializer

    def perform_create(self, serializer: MailingEmailAddressSerializer):
        """Creates a new MailingEmailAddress instance, 
        sends a confirmation email to the user, and returns the instance."""
        mailing_email_address = serializer.save()
        # send_mail_to_(mailing_email_address, self.request)
        return mailing_email_address


class MailingEmailAddressDestroyAPIView(generics.DestroyAPIView):
    """Generic destroy API view for the MailingEmailAddress model."""

    queryset = MailingEmailAddress.objects.all()
    serializer_class = MailingEmailAddressSerializer
