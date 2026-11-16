
from rest_framework import serializers
from ..models import JobPosition, Department


class JobPositionSerializer(serializers.ModelSerializer):

    department_id = serializers.PrimaryKeyRelatedField(
        source="department",
        queryset=Department.objects.all(),
        write_only=True
    )

    department_name = serializers.CharField(
        source="department.name",
        read_only=True
    )

    class Meta:
        model = JobPosition
        fields = [
            "id",
            "department_id",
            "department_name",
            "title",
            "description",
            "required_skills",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
