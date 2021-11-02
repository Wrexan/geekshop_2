from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
from datetime import datetime
from products.models import ProductCategory, Product
from baskets.models import Basket
from django.contrib.auth.decorators import login_required


def index(request):
    context = {'title': 'GeekShop111',
               'date': datetime.now()}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'GeekShop-Catalog',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()}
    return render(request, 'products/products.html', context)


@login_required
def item_add(request, id):
    if request.is_ajax():
        item = Product.objects.get(id=id)
        baskets = Basket.objects.filter(user=request.user, product=item)
        if not baskets.exists():
            Basket.objects.create(user=request.user, product=item, quantity=1)
        else:
            basket = baskets.first()
            if item.quantity - basket.quantity > 0:
                basket.quantity += 1
                basket.save()
            else:
                messages.error(request, item.name + ' - закончились.')
        baskets = Basket.objects.filter(user=request.user)
        return HttpResponse(request)

    # product = Product.objects.get(id=product_id)
    # baskets = Basket.objects.filter(user=request.user, product=product)
    # if not baskets.exists():
    #     Basket.objects.create(user=request.user, product=product, quantity=1)
    #     return HttpResponseRedirect(request.META['HTTP_REFERER'])
    # else:
    #     basket = baskets.first()
    #     if product.quantity - basket.quantity > 0:
    #         basket.quantity += 1
    #         basket.save()
    #     else:
    #         messages.error(request, product.name + ' - закончились.')
    #     return HttpResponseRedirect(request.META['HTTP_REFERER'])