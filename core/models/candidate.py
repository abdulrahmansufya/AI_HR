
from django.db import models


class Candidate(models.Model):
    full_name = models.CharField(
        max_length=150
    )
    email = models.EmailField(
        unique=True
    )
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name
