
from pathlib import Path

from rest_framework import serializers
from ..models import Resume, Candidate


class ResumeSerializer(serializers.ModelSerializer):

    candidate = serializers.PrimaryKeyRelatedField(
        queryset=Candidate.objects.all()
    )

    class Meta:
        model = Resume
        fields = [
            "id",
            "candidate",
            "file",
            "uploaded_at",
        ]
        read_only_fields = ["id", "uploaded_at"]

    def validate_file(self, value):
        allowed_extensions = [".pdf", ".docx", ".txt"]
        extension = Path(value.name).suffix.lower()

        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Only PDF, DOCX, and TXT files are allowed."
            )

        return value
