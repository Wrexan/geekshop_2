from baskets.models import Basket


def baskets(request):
    bask = []
    if request.user.is_authenticated:
        bask = Basket.objects.filter(user=request.user)
    return {
        'baskets': bask,
    }
