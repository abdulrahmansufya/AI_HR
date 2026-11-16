
from django.contrib import admin
from .models import (
    Department,
    JobPosition,
    Candidate,
    Resume,
    ScreeningResult,
    InterviewQuestionSet,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "department", "created_at")
    list_filter = ("department",)
    search_fields = ("title", "department__name")
    ordering = ("title",)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "phone", "created_at")
    search_fields = ("full_name", "email", "phone")
    ordering = ("full_name",)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "file", "uploaded_at")
    search_fields = ("candidate__full_name", "candidate__email")
    ordering = ("-uploaded_at",)


@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "candidate",
        "job_position",
        "score",
        "recommendation",
        "generated_at",
    )
    list_filter = ("recommendation", "job_position")
    search_fields = ("candidate__full_name", "job_position__title")
    ordering = ("-generated_at",)


@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "candidate",
        "job_position",
        "screening_result",
        "generated_at",
    )
    list_filter = ("job_position",)
    search_fields = ("candidate__full_name", "job_position__title")
    ordering = ("-generated_at",)

