from generic.models import BaseModel
from django.db import models


class Payment(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='%(class)s_user',
                             blank=True, null=True)
    amount = models.FloatField(max_length=32, blank=True, null=True)
    note = models.CharField(max_length=32, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    transaction_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'payments'

    def __str__(self):
        return '{} - {}'.format(self.created_by.username, self.date)

