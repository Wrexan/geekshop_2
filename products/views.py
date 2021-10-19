from django.shortcuts import render
from datetime import datetime
from products.models import ProductCategory, Product


def index(request):
    context = {'title': 'GeekShop111',
               'date': datetime.now()}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'GeekShop-Catalog',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()}
    return render(request, 'products/products.html', context)
