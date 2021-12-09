from django.contrib import admin

from products.models import ProductCategory, Product


# admin.site.register(ProductCategory)
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    # cat_num = str(ProductCategory.get_items_num())
    list_display = ('name', 'description', 'is_active')
    fields = ('name', 'description', 'is_active')
    # readonly_fields = ('description',)
    ordering = ('name', 'is_active')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'is_active')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category', 'is_active')
    # readonly_fields = ('description',)
    ordering = ('name', 'price', 'quantity', 'category')
    search_fields = ('name',)
