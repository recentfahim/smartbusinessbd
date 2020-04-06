from generic.models import BaseModel
from django.db import models


class Subscription(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='%(class)s_user',
                             blank=True, null=True)
    subscription_type = models.CharField(max_length=32, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
