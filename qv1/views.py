from django.shortcuts import render
from rest_framework.views import APIView
from qv1.models import Question, Quiz
from qv1.serialzers import QuestionSerialzers, QuizSerialzers
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class Quizview(APIView):

    def get_object(self):
        try:
            Quiz.objects.all()
        except Quiz.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request):
        queryset = self.get_object()
        serializers = QuizSerialzers(queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
