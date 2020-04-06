from generic.models import BaseModel
from django.db import models


class TempData(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='%(class)s_user',
                             blank=True, null=True)
    temp_data = models.CharField(max_length=32, blank=True, null=True)
    data_purpose = models.CharField(max_length=64, blank=True, null=True)
