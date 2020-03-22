# Generated by Django 2.2.8 on 2020-03-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EcommerceHasProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'ecommerce_has_product',
            },
        ),
        migrations.CreateModel(
            name='EcommerceSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('name', models.CharField(max_length=30)),
                ('logo', models.CharField(blank=True, max_length=30, null=True)),
                ('website', models.CharField(blank=True, max_length=30, null=True)),
                ('shop_link', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ecommerce_store',
            },
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('percentage', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'partnership',
            },
        ),
        migrations.CreateModel(
            name='SellRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'sell_record',
            },
        ),
    ]
