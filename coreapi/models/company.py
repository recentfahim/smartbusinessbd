from generic.models import BaseModel
from django.db import models
from .city import City
from .country import Country


class Company(BaseModel):
    name = models.CharField(max_length=55)
    website = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    fax = models.CharField(max_length=15, null=True, blank=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    logo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name

