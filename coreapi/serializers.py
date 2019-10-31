from rest_framework import serializers
from .models import Brand, Category, City, ContactCompany, ContactPerson, Country, CustomUser, SubCategory, Product, \
    Warehouse


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'user', 'logo', 'url', 'is_public']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'user', 'is_public']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']


class ContactCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactCompany
        fields = ['company_name', 'group_reference', 'attention', 'address_1', 'address_2', 'country', 'city',
                  'post_code', 'company_email', 'phone', 'fax', 'mobile_number', 'skype', 'website', 'supplier',
                  'customer', 'user'
                  ]


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = ['name', 'mobile_number', 'email', 'user', 'supplier', 'customer', 'company']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name', 'description', 'user', 'is_public']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['item_key', 'item_name', 'stock_alert', 'unit', 'vat', 'description', 'track',
                  'brand', 'category', 'sub_category', 'user', 'warehouse'
                  ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['name', 'address', 'phone', 'mobile_number', 'country', 'city', 'email', 'is_primary', 'user']
