from rest_framework import serializers
from .models import Partnership, EcommerceHasProduct, EcommerceSite, SellRecord
from users.serializers import UserSerializer
from inventory.serializers import ProductSerializer
from coreapi.serializers import CompanySerializer


class PartnershipSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    partner = UserSerializer(read_only=True)

    class Meta:
        model = Partnership
        fields = ['id', 'partner', 'company', 'product', 'percentage', 'created_by']


class EcommerceSiteSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = EcommerceSite
        fields = ['id', 'name', 'logo', 'website', 'shop_link', 'created_by']


class EcommerceHasProductSerializer(serializers.ModelSerializer):
    ecommerce = EcommerceSiteSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = EcommerceHasProduct
        fields = ['id', 'price', 'quantity', 'product', 'ecommerce', 'created_by']


class SellRecordSerializer(serializers.ModelSerializer):
    ecommerce_has_product = EcommerceHasProductSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = SellRecord
        fields = ['id', 'price', 'quantity', 'ecommerce_has_product', 'created_by']

