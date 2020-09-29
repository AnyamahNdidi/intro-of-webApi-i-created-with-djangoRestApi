from rest_framework import serializers
from qv1.models import Quiz, Question


class QuizSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
