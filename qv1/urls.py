from django.urls import path
from qv1.views import Quizview

urlpatterns = [
    path('quizes/', Quizview.as_view(), name="quizes"),
    ]
