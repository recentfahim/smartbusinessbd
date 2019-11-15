# Generated by Django 2.2.6 on 2019-11-15 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnership',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_user', to=settings.AUTH_USER_MODEL),
        ),
    ]