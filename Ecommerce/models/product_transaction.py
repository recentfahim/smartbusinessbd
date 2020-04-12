from generic.models import BaseModel
from inventory.models import Product, Warehouse, ProductVariant
from django.db import models
from users.models import Contact


class ProductTransaction(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='%(class)s_product',
                                blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='%(class)s_contact',
                                blank=True, null=True)
    quantity = models.CharField(max_length=32, blank=True, null=True)
    is_sell = models.BooleanField(blank=True, null=True, default=False)
    variants = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='%(class)s_variant',
                                 blank=True, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='%(class)s_warehouse',
                                  blank=True, null=True)

    class Meta:
        verbose_name = 'product_transaction'
        verbose_name_plural = 'product_transactions'
        db_table = 'product_transaction'

    def __str__(self):
        return self.product.item_name + ' # ' + self.warehouse.name
