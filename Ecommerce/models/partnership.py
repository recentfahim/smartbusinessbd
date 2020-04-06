from django.db import models
from generic.models import BaseModel
from coreapi.models import Company
from inventory.models import Product


class Partnership(BaseModel):
    partner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='%(class)s_partner',
                                blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='%(class)s_company',
                                blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='%(class)s_product',
                                blank=True, null=True)
    percentage = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'Ecommerce'

    def __str__(self):
        return '{} - {}'.format(self.created_by.username, self.percentage)
