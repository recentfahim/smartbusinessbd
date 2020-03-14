from django.db import models
from generic.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=45, null=True)
    logo = models.CharField(max_length=45, null=True, blank=True)
    url = models.CharField(max_length=45, null=True, blank=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.name
