from rest_framework import serializers
from .models import Brand, Category, City, ContactCompany, ContactPerson, Country, CustomUser, SubCategory, Product, \
    Warehouse, Company, Partnership, ProductVariant, ProductImage, VariantType, VariantTypeOption, SellRecord,\
    EcommerceHasProduct, EcommerceSite


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'phone', 'avatar']


class BrandSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'created_by', 'logo', 'url', 'is_public']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class CountrySerializer(serializers.ModelSerializer):
    country_city = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'country_city']


class ContactCompanySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    city = CitySerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = ContactCompany
        fields = ['id', 'company_name', 'group_reference', 'attention', 'address_1', 'address_2', 'country', 'city',
                  'post_code', 'company_email', 'phone', 'fax', 'mobile_number', 'skype', 'website', 'supplier',
                  'customer', 'created_by'
                  ]


class ContactPersonSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    company = ContactCompanySerializer(read_only=True)

    class Meta:
        model = ContactPerson
        fields = ['id', 'name', 'mobile_number', 'email', 'created_by', 'supplier', 'customer', 'company']


class SubCategorySerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'created_by', 'is_public']


class CategorySerializer(serializers.ModelSerializer):
    category_sub_category = SubCategorySerializer(read_only=True, many=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_by', 'is_public', 'category_sub_category']
        read_only_fields = ['get_sub_category']


class CompanySerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'email', 'address', 'city', 'region', 'postcode', 'country', 'phone', 'fax',
                  'image', 'logo', 'created_at', 'created_by']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    sub_category = SubCategorySerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'item_key', 'item_name', 'stock_alert', 'unit', 'vat', 'description', 'track',
                  'brand', 'category', 'sub_category', 'created_by', 'warehouse']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'address', 'phone', 'mobile_number', 'country', 'city', 'email', 'is_primary', 'created_by']


class VariantTypeSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = VariantType
        fields = ['id', 'name', 'created_by']


class VariantTypeOptionSerializer(serializers.ModelSerializer):
    variant_type = VariantTypeSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = VariantTypeOption
        fields = ['id', 'name', 'variant_type', 'created_by']


class ProductVariantSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    variant_type = VariantTypeSerializer(read_only=True, many=True)
    variant_type_option = VariantTypeOptionSerializer(read_only=True, many=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'purchase_price', 'selling_price', 'quantity', 'product', 'variant_type',
                  'variant_type_option', 'created_by']


class PartnershipSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)
    partner = CustomUserSerializer(read_only=True)

    class Meta:
        model = Partnership
        fields = ['id', 'partner', 'company', 'product', 'percentage', 'created_by']


class EcommerceSiteSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = EcommerceSite
        fields = ['id', 'name', 'logo', 'website', 'shop_link', 'created_by']


class EcommerceHasProductSerializer(serializers.ModelSerializer):
    ecommerce = EcommerceSiteSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = EcommerceHasProduct
        fields = ['id', 'price', 'quantity', 'product', 'ecommerce', 'created_by']


class SellRecordSerializer(serializers.ModelSerializer):
    ecommerce_has_product = EcommerceHasProductSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = SellRecord
        fields = ['id', 'price', 'quantity', 'ecommerce_has_product', 'created_by']

