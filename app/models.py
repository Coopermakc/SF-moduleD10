from django.db import models


class Car(models.Model):

    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    year = models.IntegerField()
    transmission = models.SmallIntegerField(choices=[(1, 'manual'), (2, 'automatic'), (3, 'robot')])
    color = models.CharField(max_length=10)


    def __str__(self):

        return self.manufacturer + ' ' + self.model
