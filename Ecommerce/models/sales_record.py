from django.db import models
from generic.models import BaseModel
from . import EcommerceHasProduct


class SellRecord(BaseModel):
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    ecommerce_has_product = models.ForeignKey(EcommerceHasProduct, on_delete=models.CASCADE,
                                              related_name='%(class)s_ecommerce_has_product')

    class Meta:
        db_table = 'sell_record'
