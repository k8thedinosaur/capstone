from django import forms
from .models import Item, ShopItem


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'quantity', 'date_added', 'expires', 'calories', 'intended_use']


class ShopForm(forms.ModelForm):
    class Meta:
        model = ShopItem
        fields = ['name', 'number']


class DeleteItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = []


class DeleteShoppingForm(forms.ModelForm):
    class Meta:
        model = ShopItem
        fields = []
