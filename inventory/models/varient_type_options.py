from django.db import models
from generic.models import BaseModel
from .varient_type import VariantType


class VariantTypeOption(BaseModel):
    name = models.CharField(max_length=50)
    variant_type = models.ForeignKey(VariantType, blank=True, null=True, on_delete=models.CASCADE,
                                     related_name='%(class)s_variant_type')

    class Meta:
        db_table = 'variant_type_option'

    def __str__(self):
        return self.name
