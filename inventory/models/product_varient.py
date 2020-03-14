from django.db import models
from generic.models import BaseModel
from .product import Product
from .varient_type import VariantType
from .varient_type_options import VariantTypeOption


class ProductVariant(BaseModel):
    name = models.CharField(max_length=50)
    purchase_price = models.IntegerField(blank=True, null=True)
    selling_price = models.IntegerField(blank=True, null=True)
    quantity = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='%(class)s_product')
    variant_type = models.ForeignKey(VariantType, blank=True, null=True, on_delete=models.CASCADE,
                                     related_name='%(class)s_variant_type')
    variant_type_option = models.ForeignKey(VariantTypeOption, blank=True, null=True, on_delete=models.CASCADE,
                                            related_name='%(class)s_variant_type_option')

    class Meta:
        db_table = 'variant'

    def __str__(self):
        return self.name
