
from django.urls import path

from .views import (
    create_department,
    create_job_position,
    create_candidate,
    upload_resume,
    get_screening_result,
    get_interview_questions
)

urlpatterns = [
    path("departments/", create_department, name="department-create"),
    path("job-positions/", create_job_position, name="job-position-create"),
    path("candidates/", create_candidate, name="candidate-create"),
    path("resumes/", upload_resume, name="resume-upload"),
    path("screening-results/<int:pk>/", get_screening_result, name="screening-result-detail"),
    path("interview-questions/<int:pk>/", get_interview_questions, name="interview-question-detail"),
]