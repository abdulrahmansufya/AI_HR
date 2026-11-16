
from django.db import models
from .candidate import Candidate

class Resume(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="resumes"
    )
    file = models.FileField(
        upload_to="resumes/"
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"Resume - {self.candidate.full_name}"
