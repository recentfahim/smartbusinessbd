from django.db import models
from generic.models import BaseModel
from inventory.models import Product
from .ecommerce_site import EcommerceSite


class EcommerceHasProduct(BaseModel):
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='%(class)s_product')
    ecommerce = models.ForeignKey(EcommerceSite, blank=True, null=True, on_delete=models.CASCADE,
                                  related_name='%(class)s_online_store')

    class Meta:
        db_table = 'ecommerce_has_product'

    def __str__(self):
        return '{product} - {ecommerce}'.format(product=self.product, ecommerce=self.ecommerce)

