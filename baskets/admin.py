from django.contrib import admin

from baskets.models import Basket
# from users.models import User


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0

#
# class ActKeyExpShow(admin.FieldListFilter):
#     model = Basket
#     fields = ('product',)
#     # model = User
#     # fields = ('activation_key',)
