from django.db import models

class Task(models.Model):
    date = models.Model("Дата публикации")
    tittle = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")
    contact = models.TextField("Контакты")
    def __str__(self):
        return self.tittle

