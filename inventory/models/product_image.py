from django.db import models
from generic.models import BaseModel
from .product import Product
from .product_varient import ProductVariant


class ProductImage(BaseModel):
    image_path = models.CharField(max_length=50)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE,
                                related_name='%(class)s_product')
    variant = models.ForeignKey(ProductVariant, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='%(class)s_variant')

    class Meta:
        db_table = 'product_image'

    def __str__(self):
        return self.image_path
