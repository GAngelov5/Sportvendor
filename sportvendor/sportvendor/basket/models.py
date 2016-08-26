from django.db import models
from items.models import Item
from django.conf import settings
# from django.contrib.auth.models import User

# Create your models here.


class BasketManager(models.Manager):

    def create_basket(self, current_user):
        basket_name = current_user.first_name[0] + "'s basket"
        initial_size = 50
        new_basket = Basket(name=basket_name,
                            size=initial_size,
                            user=current_user)
        new_basket.save()

    def get_basket_items(self, basket_pk):
        basket = Basket.objects.get(id=basket_pk)
        return basket.basket_items.all()

    def get_basket_amount(self, basket_pk):
        basket = Basket.objects.get(id=basket_pk)
        total_amount = 0
        for item in basket.basket_items.all():
            total_amount += item.price
        return total_amount


class Basket(models.Model):
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    create_date = models.DateField(auto_now=True)
    basket_items = models.ManyToManyField(Item)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True)

    objects = BasketManager()

    def __str__(self):
        return self.name
