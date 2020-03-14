from django.db import models
from generic.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    is_public = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name