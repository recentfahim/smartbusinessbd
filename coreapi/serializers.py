from rest_framework import serializers
from .models import City, Country, Company
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


class CompanySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'email', 'address', 'city', 'region', 'postcode', 'country', 'phone', 'fax',
                  'image', 'logo', 'created_at', 'created_by']
