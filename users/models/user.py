from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from coreapi.models import City, Country


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractUser):
    SUPER_ADMIN = 'sp'
    ADMIN = 'ad'
    USER = 'us'

    USER_TYPE_CHOICES = (
        (SUPER_ADMIN, 'Super Admin'),
        (ADMIN, 'Admin'),
        (USER, 'User')
    )
    role = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default=USER)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.CharField(null=True, max_length=55, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True,  related_name='%(class)s_city')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='%(class)s_country')
    trail_start_date = models.DateTimeField(null=True, blank=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
