from django.db import models


class Mode1(models.Model):
    pole1 = models.IntegerField()
    pole2 = models.CharField(max_length=45)
    pole3 = models.TextField()

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"

    def __str__(self):
        return str(self.pole2) + ' ' + str(self.pole1)


class Mode2(models.Model):
    pole1 = models.IntegerField()
    pole2 = models.CharField(max_length=20)
    # pole3 = models.ForeignKey(Mode1, models.CASCADE)
    pole4 = models.ManyToManyField(Mode1)

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"

    def __str__(self):
        return str(self.pole2) + ' ' + str(self.pole1)



