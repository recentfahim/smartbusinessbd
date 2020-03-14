from django.db import models
from .country import Country


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='%(class)s_country')

    class Meta:
        db_table = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name
