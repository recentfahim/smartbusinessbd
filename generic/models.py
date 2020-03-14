from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    created_by = models.ForeignKey('users.User', related_name='%(class)s_created_by', on_delete=models.DO_NOTHING,
                                   blank=True, null=True)
    updated_by = models.ForeignKey('users.User', related_name='%(class)s_updated_by', on_delete=models.DO_NOTHING,
                                   blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    deleted_by = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='%(class)s_deleted_by')

    class Meta:
        abstract = True

    def get_url_name(self, suffix):
        return self._meta.label_lower.replace('.', ':') + f'_{suffix}'

    def get_create_url(self):
        url_name = self.get_url_name('create')
        return reverse(url_name)

    def get_list_url(self):
        url_name = self.get_url_name('list')
        return reverse(url_name)

    def get_detail_url(self):
        url_name = self.get_url_name('detail')
        return reverse(url_name, args=[self.pk])

    def get_update_url(self):
        url_name = self.get_url_name('update')
        return reverse(url_name, args=[self.pk])

