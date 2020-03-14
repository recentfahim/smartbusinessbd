from rest_framework import serializers
from .models import City, Country, Warehouse, Company
from inventory.models import Brand, Category, Product, VariantType, ProductVariant, VariantTypeOption
from users.models import Contact, User
from partnership.models import Partnership, EcommerceHasProduct, EcommerceSite, SellRecord
from users.serializers import UserSerializer


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
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'company_name', 'group_reference', 'attention', 'address_1', 'address_2', 'country', 'city',
                  'post_code', 'company_email', 'phone', 'fax', 'mobile_number', 'skype', 'website', 'supplier',
                  'customer', 'created_by'
                  ]


class CategorySerializerForSubCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'is_public']


class CompanySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'email', 'address', 'city', 'region', 'postcode', 'country', 'phone', 'fax',
                  'image', 'logo', 'created_at', 'created_by']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'address', 'phone', 'mobile_number', 'country', 'city', 'email', 'is_primary',
                  'created_by'
                  ]
