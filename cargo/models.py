from django.db import models


class Cargo(models.Model):
    pick_up = models.CharField(max_length=155)
    delivery = models.CharField(max_length=155)
    weight = models.PositiveSmallIntegerField()
    description = models.TextField()



