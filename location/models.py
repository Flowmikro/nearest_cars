from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255)
    state_name = models.CharField(max_length=255)
    zip = models.PositiveIntegerField()
    lat = models.DecimalField(max_digits=10, decimal_places=5)
    lng = models.DecimalField(max_digits=10, decimal_places=5)
