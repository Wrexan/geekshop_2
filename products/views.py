from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html')


def products(request):
    context = {'title': 'GeekShop-Catalog'}
    return render(request, 'products/product.html')