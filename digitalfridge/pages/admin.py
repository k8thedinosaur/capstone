from django.contrib import admin
from pages.models import Item, Fridge, ShopItem

admin.site.register(Fridge)
admin.site.register(Item)
admin.site.register(ShopItem)