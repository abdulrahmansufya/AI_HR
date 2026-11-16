
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import InterviewQuestionSet
from ..serializers import InterviewQuestionSetSerializer


@api_view(["GET"])
def get_interview_questions(request, pk):
    try:
        question_set = InterviewQuestionSet.objects.get(pk=pk)

    except InterviewQuestionSet.DoesNotExist:
        return Response(
            {"error": "Interview question set not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = InterviewQuestionSetSerializer(question_set)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )
