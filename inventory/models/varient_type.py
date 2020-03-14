from django.db import models
from generic.models import BaseModel


class VariantType(BaseModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'variant_type'

    def __str__(self):
        return self.name
