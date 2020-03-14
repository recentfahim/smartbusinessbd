from django.db import models
from generic.models import BaseModel


class EcommerceSite(BaseModel):
    name = models.CharField(max_length=30)
    logo = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=30, blank=True, null=True)
    shop_link = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'ecommerce_store'

    def __str__(self):
        return self.name
