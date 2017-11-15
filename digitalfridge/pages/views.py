from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import ItemForm, ShopForm
from .models import Item, ShopItem


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
    tossed = Item.objects.filter(tossed__exact=True)
    shop_item = ShopItem.objects.all()

    # if request.method == "POST":
    #     add_form = ItemForm(request.POST)
    #     if add_form.is_valid():
    #         add_form.save()
    #         return redirect('/')
    # else:
    #     add_form = ItemForm()

    if request.method == "POST":
        shop_form = ShopForm(request.POST)
        if shop_form.is_valid():
            shop_form.save()
            return redirect('/')
    else:
        shop_form = ShopForm()
    return render(request, 'pages/home.html', {'contents': contents, 'frozen': frozen, 'heatneat': heatneat, 'desserts': desserts, 'meat': meat, 'seafood': seafood, 'dairy': dairy, 'veg': veg, 'fruit': fruit, 'leftovers': leftovers, 'alcohol': alcohol, 'nonedible': nonedible, 'other': other, 'condiments': condiments, 'sauces': sauces, 'beverages': beverages, 'tossed': tossed, 'shop_item': shop_item, 'shop_form': shop_form})

    # 'add_form': add_form},
