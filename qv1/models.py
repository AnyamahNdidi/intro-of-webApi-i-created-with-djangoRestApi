from django.db import models



class Quiz(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(verbose_name="description", null=True)
    created_data = models.DateField(auto_now=True)
    url = models.URLField(verbose_name="url", null=True)


class Question(models.Model):

    question = models.TextField(verbose_name="question", null=False)
    choice = models.TextField(verbose_name="choice", null=False)
    choice1 = models.TextField(verbose_name="choice1", null=False)
    choice2 = models.TextField(verbose_name="choice2", null=False)
    choice3 = models.TextField(verbose_name="choice3", null=False)
    answer = models.CharField(max_length=10)
