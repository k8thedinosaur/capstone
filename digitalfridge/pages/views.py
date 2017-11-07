from django.shortcuts import render
from pages.models import Item, Fridge


def home(request):
    contents = Item.objects.all()
    unknown = Item.objects.filter(category__exact='Unknown')
    # context = {'contents': contents}
    return render(request, 'pages/home.html', {'contents': contents})
