from django.db import models
from django.utils.functional import cached_property

from users.models import User
from products.models import Product


class BasketQuerySet(models.QuerySet):
    def delete(self):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(self.__class__, self).delete()


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    @property
    def sum(self):
        return self.product.price * self.quantity

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    # @property
    # def user_basket(self):
    #     return Basket.objects.filter(user=self.user)

    @property
    def total_sum(self):
        return sum(basket.sum for basket in self.get_items_cached)

    @property
    def total_quantity(self):
        return sum(basket.quantity for basket in self.get_items_cached)

    # def delete(self):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super(self.__class__, self).delete()

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)
