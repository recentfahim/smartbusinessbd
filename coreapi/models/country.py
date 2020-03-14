from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name
