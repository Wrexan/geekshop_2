from django.shortcuts import render
import os
import json

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.


def index(request):
    context = {'title': 'GeekShop111'}
    return render(request, 'products/index.html', context)


def products(request):
    items = json.load(open(os.path.join(MODULE_DIR, 'fixtures/products.json'), encoding='utf-8'))
    # for i in items:
    #
    context = {'title': 'GeekShop-Catalog',
               'products': items}
    return render(request, 'products/products.html', context)
