from django.db import models


class Fridge(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ShopItem(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Item(models.Model):
    fridge = models.ForeignKey('Fridge', related_name='fridge', default=1)
    meat = 'Meat'
    seafood = 'Seafood'
    dairy = 'Dairy'
    veg = 'Veg'
    fruit = 'Fruit'
    leftovers = 'Leftovers'
    alcohol = 'Alcohol'
    nonedible = 'Non-Edible'
    other = 'Other'
    condiments = 'Condiments'
    sauces = 'Sauces'
    beverages = 'Beverages'
    frozen = 'Frozen'
    heatneat = 'Heat-n-Eat'
    desserts = 'Desserts'
    CATEGORY_CHOICES = (
        (meat, 'Meat'),
        (seafood, 'Seafood'),
        (dairy, 'Dairy'),
        (veg, 'Veg'),
        (fruit, 'Fruit'),
        (leftovers, 'Leftovers'),
        (alcohol, 'Alcohol'),
        (nonedible, 'Non-Edible'),
        (other, 'Other'),
        (condiments, 'Condiments'),
        (sauces, 'Sauces'),
        (beverages, 'Beverages'),
        (frozen, 'Frozen'),
        (heatneat, 'Heat-n-Eat'),
        (desserts, 'Desserts'),
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Other',
    )
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1, verbose_name='Quantity/Servings')
    date_added = models.DateField()
    expires = models.DateField()
    calories = models.IntegerField(blank=True, null=True)
    intended_use = models.CharField(max_length=255, blank=True, null=True)
    tossed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

