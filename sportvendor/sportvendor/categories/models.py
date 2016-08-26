from django.db import models
from items.models import Item


class CategoryManager(models.Manager):
    def get_category_items(self, category_pk):
        category = Category.objects.get(id=category_pk)
        return category.category_items.all()


class Category(models.Model):
    name = models.CharField(max_length=50)
    stars = models.IntegerField()
    season_discount = models.IntegerField()
    category_items = models.ManyToManyField(Item)

    objects = CategoryManager()

    def __str__(self):
        return self.name
