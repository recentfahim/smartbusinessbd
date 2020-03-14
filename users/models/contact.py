from django.db import models
from generic.models import BaseModel
from coreapi.models import Country,  City


class Contact(BaseModel):
    name = models.CharField(max_length=50)
    group_reference = models.CharField(max_length=50, blank=True, null=True)
    attention = models.CharField(max_length=50, blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='%(class)s_country')
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_city')
    post_code = models.CharField(max_length=5, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=50, blank=True, null=True)
    skype = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    is_supplier = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=True)
    is_company = models.BooleanField(default=False)

    class Meta:
        db_table = 'contact_company'
        verbose_name_plural = 'Contact Companies'

    def __str__(self):
        return self.name

