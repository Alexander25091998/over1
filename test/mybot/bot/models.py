from django.db import models


class Quiz(models.Model):
    question = models.CharField(max_length=255)
    answers = models.CharField(max_length=255)

