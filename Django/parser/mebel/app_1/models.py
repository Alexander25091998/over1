from django.db import models

class Mebel(models.Model):
    link = models.TextField('Ссылка')
    price = models.DecimalField('Цена', decimal_places=1, max_digits=12)
    description = models.TextField('Описание')

    def __str__(self):
        return f"{self.price} | {self.description[:30]}"