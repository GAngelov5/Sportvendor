from django.db import models
from django.conf import settings
from items.models import Item
from discount.models import Discount


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    items_history = models.ManyToManyField(Item)
    discounts = models.ManyToManyField(Discount)
