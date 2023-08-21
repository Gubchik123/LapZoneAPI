from rest_framework import serializers

from .models import MailingEmailAddress


class MailingEmailAddressSerializer(serializers.ModelSerializer):
    """Model serializer for the MailingEmailAddress model."""

    class Meta:
        """Meta options for the MailingEmailAddressSerializer."""

        fields = "__all__"
        model = MailingEmailAddress
        read_only_fields = ["id", "created"]
