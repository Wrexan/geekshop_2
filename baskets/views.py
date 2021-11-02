from django.shortcuts import HttpResponseRedirect
from django.contrib import messages

from products.models import Product
from baskets.models import Basket


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket = baskets.first()
        if product.quantity - basket.quantity > 0:
            basket.quantity += 1
            basket.save()
        else:
            messages.error(request, product.name + ' - закончились.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, id):
    product = Basket.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
