from django.shortcuts import render
from pages.models import Item, Fridge


# def home(request):
#     contents = Item.objects.all()
#     unknown = Item.objects.filter(category__in='Unknown')
#     # context = {'contents': contents}
#     return render(request, 'pages/home.html', {'contents': contents, 'unknown': unknown})

def home(request):
    contents = Item.objects.all()
    unknown = Item.objects.filter(category__startswith='Unknown')
    return render(request, 'pages/home.html', {'contents': contents, 'unknown': unknown})
