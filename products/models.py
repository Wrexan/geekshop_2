from django.db import models
# from django.utils.functional import cached_property


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(max_length=256, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_items_num():
        # return ProductCategory.objects.order_by('name')
        items = Product.objects.select_related()
        return len(items)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(verbose_name='имя продукта', max_length=256, unique=True)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=60, blank=True,)
    description = models.TextField(verbose_name='описание', max_length=256, blank=True, null=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='активен', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
        # a = (self.name, self.category).select_related()
        # return f'{self.name} | {self.category}'

    @staticmethod
    def get_items():
        # if cat:
        #     return len(Product.objects.filter(is_active=True, quantity__gte=1, category=cat).order_by('name'))
        # else:
        return Product.objects.filter(is_active=True, quantity__gte=1).order_by('category', 'name')

    class Meta:
        ordering = ['-updated']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
