from django.db import models

class Person(models.Model):
    name = models.CharField('Название авто', max_length=30),

