from django.contrib import admin

from baskets.models import Basket
# from users.models import User


@admin.register(Basket)
class BasketsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'user',)
                    # 'status',
                    # 'get_total_quantity', 'get_total_cost',
                    # 'created', 'updated', 'is_active',)


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
