from django.shortcuts import render, redirect
from .forms import ItemForm, ShopForm
from .models import Item, ShopItem


def home(request):
    contents = Item.objects.all()
    frozen = Item.objects.filter(category__startswith='Frozen', tossed__exact=False)
    heatneat = Item.objects.filter(category__startswith='Heat', tossed__exact=False)
    desserts = Item.objects.filter(category__startswith='Desserts', tossed__exact=False)
    meat = Item.objects.filter(category__startswith='Meat', tossed__exact=False)
    seafood = Item.objects.filter(category__startswith='Seafood', tossed__exact=False)
    dairy = Item.objects.filter(category__startswith='Dairy', tossed__exact=False)
    veg = Item.objects.filter(category__startswith='Veg', tossed__exact=False)
    fruit = Item.objects.filter(category__startswith='Fruit', tossed__exact=False)
    leftovers = Item.objects.filter(category__startswith='Leftovers', tossed__exact=False)
    alcohol = Item.objects.filter(category__startswith='Alcohol', tossed__exact=False)
    nonedible = Item.objects.filter(category__startswith='Non', tossed__exact=False)
    other = Item.objects.filter(category__startswith='Other', tossed__exact=False)
    condiments = Item.objects.filter(category__startswith='Condiments', tossed__exact=False)
    sauces = Item.objects.filter(category__startswith='Sauces', tossed__exact=False)
    beverages = Item.objects.filter(category__startswith='Bev', tossed__exact=False)
    tossed = Item.objects.filter(tossed__exact=True).order_by('date_added')
    shop_item = ShopItem.objects.all()

    if request.GET.get('DeleteButton'):
        Item.objects.filter(id=request.GET.get('DeleteButton')).delete()
        return redirect('/')

    if request.GET.get('ShopDeleteButton'):
        ShopItem.objects.filter(id=request.GET.get('ShopDeleteButton')).delete()
        return redirect('/')

    if request.GET.get('TossedButton'):
        Item.objects.filter(id=request.GET.get('TossedButton')).update(tossed=True)
        return redirect('/')

    if 'TossedClearButton' in request.POST:
        tossed.delete()
        return redirect('/')

    if 'addButton' in request.POST:
        add_form = ItemForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('/')

    if 'shopButton' in request.POST:
        shop_form = ShopForm(request.POST)
        if shop_form.is_valid():
            shop_form.save()
            return redirect('/')

    else:
        add_form = ItemForm()
        shop_form = ShopForm()
    return render(request, 'pages/home.html', {'contents': contents, 'frozen': frozen, 'heatneat': heatneat, 'desserts': desserts, 'meat': meat, 'seafood': seafood, 'dairy': dairy, 'veg': veg, 'fruit': fruit, 'leftovers': leftovers, 'alcohol': alcohol, 'nonedible': nonedible, 'other': other, 'condiments': condiments, 'sauces': sauces, 'beverages': beverages, 'tossed': tossed, 'shop_item': shop_item, 'add_form': add_form, 'shop_form': shop_form})
