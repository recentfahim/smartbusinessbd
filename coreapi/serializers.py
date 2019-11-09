from rest_framework import serializers
from .models import Brand, Category, City, ContactCompany, ContactPerson, Country, CustomUser, SubCategory, Product, \
    Warehouse


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'phone', 'avatar']


class BrandSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'user', 'logo', 'url', 'is_public']


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
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = ContactCompany
        fields = ['id', 'company_name', 'group_reference', 'attention', 'address_1', 'address_2', 'country', 'city',
                  'post_code', 'company_email', 'phone', 'fax', 'mobile_number', 'skype', 'website', 'supplier',
                  'customer', 'user'
                  ]


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = ['id', 'name', 'mobile_number', 'email', 'user', 'supplier', 'customer', 'company']


class SubCategorySerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'user', 'is_public']


class CategorySerializer(serializers.ModelSerializer):
    category_sub_category = SubCategorySerializer(read_only=True, many=True)
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'user', 'is_public', 'category_sub_category']
        read_only_fields = ['get_sub_category']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'item_key', 'item_name', 'stock_alert', 'unit', 'vat', 'description', 'track',
                  'brand', 'category', 'sub_category', 'user', 'warehouse'
                  ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'address', 'phone', 'mobile_number', 'country', 'city', 'email', 'is_primary', 'user']
