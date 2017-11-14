from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'quantity', 'date_added', 'expires', 'calories', 'intended_use']