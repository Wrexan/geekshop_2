import json
import os

from django.core.management.base import BaseCommand

# from users.models import User
from products.models import ProductCategory, Product

JSON_PATH = 'products/fixtures'
JSON_CAT_NAME = 'categories'
JSON_ITM_NAME = 'goods'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json(JSON_CAT_NAME)

        ProductCategory.objects.all().delete()

        for category in categories:
            new_category = ProductCategory(**category['fields'])
            new_category.pk = category['pk']
            new_category.save()

        products = load_from_json(JSON_ITM_NAME)

        Product.objects.all().delete()
        for product in products:
            category_id = product['fields']['category']
            _category = ProductCategory.objects.get(pk=category_id)
            product['fields']['category'] = _category
            new_product = Product(**product['fields'])
            new_product.pk = product['pk']  # comment to prevent over-wright items in db (if they exist)
            new_product.save()

# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         categories = load_from_json('categories')
#
#         ProductCategory.objects.all().delete()
#         for category in categories:
#             new_category = ProductCategory(**category)
#             new_category.save()
#
#         products = load_from_json('products')
#
#         Product.objects.all().delete()
#         for product in products:
#             category_name = product['category']
#             _category = ProductCategory.objects.get(name=category_name)
#             product['category'] = _category
#             new_product = Product(**product)
#             new_product.save()

        # super_user = ShopUser.objects.create_superuser('admin', 'admin@geekshop.local', '123', age=30)
        # if super_user:
        #     print("Super user created.")
