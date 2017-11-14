from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from pages.models import Item, Fridge
from pages.forms import ItemForm


def home(request):
    contents = Item.objects.all()
    frozen = Item.objects.filter(category__startswith='Frozen')
    heatneat = Item.objects.filter(category__startswith='Heat')
    desserts = Item.objects.filter(category__startswith='Desserts')
    meat = Item.objects.filter(category__startswith='Meat')
    seafood = Item.objects.filter(category__startswith='Seafood')
    dairy = Item.objects.filter(category__startswith='Dairy')
    veg = Item.objects.filter(category__startswith='Veg')
    fruit = Item.objects.filter(category__startswith='Fruit')
    leftovers = Item.objects.filter(category__startswith='Leftovers')
    alcohol = Item.objects.filter(category__startswith='Alcohol')
    nonedible = Item.objects.filter(category__startswith='Non')
    other = Item.objects.filter(category__startswith='Other')
    condiments = Item.objects.filter(category__startswith='Condiments')
    sauces = Item.objects.filter(category__startswith='Sauces')
    beverages = Item.objects.filter(category__startswith='Beverages')
    return render(request, 'pages/home.html', {'contents': contents, 'frozen': frozen, 'heatneat': heatneat, 'desserts': desserts, 'meat': meat, 'seafood': seafood, 'dairy': dairy, 'veg': veg, 'fruit': fruit, 'leftovers': leftovers, 'alcohol': alcohol, 'nonedible': nonedible, 'other': other, 'condiments': condiments, 'sauces': sauces, 'beverages': beverages})

def add_model(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.isvalid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
    else:
        form = ItemForm()
        return render(request, 'pages/home.html', {'form': form})