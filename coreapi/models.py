from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CustomUser(AbstractUser):
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

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_city')

    class Meta:
        db_table = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class ContactCompany(models.Model):
    company_name = models.CharField(max_length=50)
    group_reference = models.CharField(max_length=50, blank=True, null=True)
    attention = models.CharField(max_length=50, blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='contact_company_country')
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True, related_name='contact_company_city')
    post_code = models.CharField(max_length=5, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=50, blank=True, null=True)
    skype = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    supplier = models.BooleanField(default=True)
    customer = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contact_company_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='contact_company_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='contact_company_deleted_by')

    class Meta:
        db_table = 'contact_company'
        verbose_name_plural = 'Contact Companies'

    def __str__(self):
        return self.company_name


class Category(models.Model):
    name = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='category_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='category_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='category_deleted_by')

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_sub_category', blank=True,
                                 null=True)
    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sub_category_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='sub_category_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='sub_category_deleted_by')

    class Meta:
        db_table = 'sub_category'
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=45, null=True)
    logo = models.CharField(max_length=45, null=True, blank=True)
    url = models.CharField(max_length=45, null=True, blank=True)
    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='brand_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='brand_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='brand_deleted_by')

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.name


class ContactPerson(models.Model):
    name = models.CharField(null=True, max_length=30)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    supplier = models.BooleanField(default=True)
    customer = models.BooleanField(default=True)
    company = models.ForeignKey(ContactCompany, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='contact_person_company')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contact_person_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='contact_person_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='contact_person_deleted_by')

    class Meta:
        db_table = 'contact_person'

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=15)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='warehouse_county')
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE, related_name='warehouse_city')
    email = models.EmailField(max_length=50, blank=True, null=True)
    is_primary = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='warehouse_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='warehouse_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='warehouse_deleted_by')

    class Meta:
        db_table = 'warehouse'

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=55)
    website = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    fax = models.CharField(max_length=15, null=True, blank=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    logo = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='company_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='company_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='company_deleted_by')

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Product(models.Model):
    item_key = models.CharField(max_length=10, blank=True, null=True)
    item_name = models.CharField(max_length=30, null=True)
    stock_alert = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    track = models.CharField(max_length=30, blank=True, null=True)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE, related_name='product_brand')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE,
                                 related_name='product_category')
    sub_category = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.CASCADE,
                                     related_name='product_subcategory')
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True, on_delete=models.CASCADE,
                                  related_name='product_warehouse')
    company = models.ForeignKey(Company, blank=True, null=True, related_name='company_product',
                                on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='product_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='product_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='product_deleted_by')

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.item_name


class EcommerceSite(models.Model):
    name = models.CharField(max_length=30)
    logo = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=30, blank=True, null=True)
    shop_link = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ecommerce_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='ecommerce_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='ecommerce_deleted_by')

    class Meta:
        db_table = 'ecommerce_store'

    def __str__(self):
        return self.name


class EcommerceHasProduct(models.Model):
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='online_store_has_product')
    ecommerce = models.ForeignKey(EcommerceSite, blank=True, null=True, on_delete=models.CASCADE,
                                  related_name='online_store_product')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ecommerce_product_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='ecommerce_product_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='ecommerce_product_deleted_by')

    class Meta:
        db_table = 'ecommerce_has_product'

    def __str__(self):
        return '{product} - {ecommerce}'.format(product=self.product, ecommerce=self.ecommerce)


class SellRecord(models.Model):
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    ecommerce_has_product = models.ForeignKey(EcommerceHasProduct, on_delete=models.CASCADE,
                                              related_name='product_sell_record')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sell_record_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='sell_record_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='sell_record_deleted_by')

    class Meta:
        db_table = 'sell_record'


class Partnership(models.Model):
    partner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='partner_user', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_partnership',
                                blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_partnership',
                                blank=True, null=True)
    percentage = models.CharField(max_length=5, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='partnership_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='partnership_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='partnership_deleted_by')

    class Meta:
        db_table = 'partnership'

    def __str__(self):
        return '{} - {}'.format(self.created_by.username, self.percentage)


class VariantType(models.Model):
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='variant_type_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='variant_type_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='variant_type_deleted_by')

    class Meta:
        db_table = 'variant_type'

    def __str__(self):
        return self.name


class VariantTypeOption(models.Model):
    name = models.CharField(max_length=50)
    variant_type = models.ForeignKey(VariantType, blank=True, null=True, on_delete=models.CASCADE,
                                     related_name='variant_type_option')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='variant_type_option_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='variant_type_option_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='variant_type_option_deleted_by')

    class Meta:
        db_table = 'variant_type_option'

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    name = models.CharField(max_length=50)
    purchase_price = models.IntegerField(blank=True, null=True)
    selling_price = models.IntegerField(blank=True, null=True)
    quantity = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='product_variant')
    variant_type = models.ForeignKey(VariantType, blank=True, null=True, on_delete=models.CASCADE,
                                     related_name='product_variant_type')
    variant_type_option = models.ForeignKey(VariantTypeOption, blank=True, null=True, on_delete=models.CASCADE,
                                            related_name='product_variant_option')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='variant_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='variant_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='variant_deleted_by')

    class Meta:
        db_table = 'variant'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image_path = models.CharField(max_length=50)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='product_image')
    variant = models.ForeignKey(ProductVariant, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='variant_image')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='product_image_created_by')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='product_image_updated_by')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='product_image_deleted_by')

    class Meta:
        db_table = 'product_image'

    def __str__(self):
        return self.image_path
