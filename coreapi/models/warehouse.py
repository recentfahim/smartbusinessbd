from django.db import models
from . import Country, City
from generic.models import BaseModel


class Warehouse(BaseModel):
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=15)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='%(class)s_county')
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE, related_name='%(class)s_city')
    email = models.EmailField(max_length=50, blank=True, null=True)
    is_primary = models.BooleanField(default=False)

    class Meta:
        db_table = 'warehouse'

    def __str__(self):
        return self.name
