from django.db import models

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
