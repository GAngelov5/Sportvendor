from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=100)
    discount = models.IntegerField(default=0)
    category = models.CharField(max_length=30, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    season = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
