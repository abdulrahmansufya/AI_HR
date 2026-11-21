
import re

from rest_framework import serializers
from ..models import Candidate


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_phone(self, value):
        if not value:
            return value

        if not re.fullmatch(r"\+?[0-9\s()-]+", value):
            raise serializers.ValidationError(
                "Enter a valid phone number."
            )

        digits = re.sub(r"\D", "", value)

        if not 7 <= len(digits) <= 15:
            raise serializers.ValidationError(
                "Phone number must contain between 7 and 15 digits."
            )

        return value
