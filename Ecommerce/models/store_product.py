from django.db import models
from generic.models import BaseModel
from inventory.models import ProductVariant, Product
from .ecommerce_site import EcommerceSite


class StoreProduct(BaseModel):
    price = models.FloatField(blank=True, null=True)
    quantity = models.CharField(max_length=32, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='%(class)s_product',
                                blank=True, null=True)
    ecommerce = models.ForeignKey(EcommerceSite, on_delete=models.CASCADE, related_name='%(class)s_ecommerce',
                                  blank=True, null=True)
    variants = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='%(class)s_variant',
                                 blank=True, null=True)
