from django.db import models
from brand.models import Brand


# Create your models here.


class ItemManager(models.Manager):
    def get_item(self, item_pk):
        try:
            item = Item.objects.get(pk=item_pk)
        except Item.DoesNotExist:
            item = None
        return item


class Item(models.Model):
    QUALITY_CHOICES = (
        ('G', 'Good'),
        ('B', 'Bad'),
        ('E', 'Excellent')
    )
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )
    name = models.CharField(max_length=50)
    made_from = models.CharField(max_length=400)
    size = models.CharField(max_length=1, choices=SIZES, default='S')
    added_on = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    quality = models.CharField(max_length=1, choices=QUALITY_CHOICES)
    image = models.ImageField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)

    objects = ItemManager()

    def __str__(self):
        return self.name
