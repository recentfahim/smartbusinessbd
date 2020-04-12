from django.db import models
from generic.models import BaseModel
from . import Brand, Category, Warehouse
from coreapi.models import Company


class Product(BaseModel):
    item_key = models.CharField(max_length=10, blank=True, null=True)
    item_name = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=10, null=True)
    stock_alert = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    track = models.CharField(max_length=30, blank=True, null=True)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE, related_name='%(class)s_brand')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE,
                                 related_name='%(class)s_category')
    sub_category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE,
                                     related_name='%(class)s_sub_category')
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True, on_delete=models.CASCADE,
                                  related_name='%(class)s_warehouse')
    company = models.ForeignKey(Company, blank=True, null=True, related_name='%(class)s_company',
                                on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.item_name
