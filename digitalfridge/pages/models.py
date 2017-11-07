from django.db import models


class Fridge(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    fridge = models.ForeignKey('Fridge', related_name='fridge', default=1)
    Fruit = 'Fruit'
    Veg = 'Veg'
    Meat = 'Meat'
    Unknown = 'Unknown'
    CATEGORY_CHOICES = (
        (Fruit, 'Fruit'),
        (Veg, 'Veg'),
        (Meat, 'Meat'),
        (Unknown, 'Unknown'),
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Unknown',
    )
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1, verbose_name='Quantity/Servings')
    date_added = models.DateField()
    expires = models.DateField()
    calories = models.IntegerField(blank=True, null=True)
    intended_use = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
