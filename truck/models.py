import random
import string
from django.db import models


class Truck(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.sku:
            self.sku = self.random_sku()

    def random_sku(self):
        num = random.randint(1000, 9999)
        letter = random.choice(string.ascii_uppercase)
        return f"{num}{letter}"

    load_capacity = models.PositiveSmallIntegerField()
    sku = models.CharField(max_length=5, unique=True, blank=True)