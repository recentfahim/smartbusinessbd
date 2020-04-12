from django.db import models
from inventory.models import Product, ProductVariant, Warehouse
from generic.models import BaseModel
from .ecommerce_site import EcommerceSite


class StoreProductTransaction(BaseModel):
    quantity = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='%(class)s_product',
                                blank=True, null=True)
    is_product_to_store_product = models.BooleanField(blank=True, null=True)
    ecommerce = models.ForeignKey(EcommerceSite, on_delete=models.CASCADE, related_name='%(class)s_ecommerce',
                                  blank=True, null=True)
    variants = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='%(class)s_variant',
                                 blank=True, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='%(class)s_warehouse',
                                  blank=True, null=True)

    class Meta:
        db_table = 'store_product_transaction'

    def __str__(self):
        return '{} # {}'.format(self.product, self.warehouse.name)

