from rest_framework import serializers
from .models import Category, Brand, Product, VariantType, VariantTypeOption, ProductVariant
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'parent']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'name', 'logo', 'url']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'item_key', 'item_name', 'stock_alert', 'unit', 'vat', 'description', 'track',
                  'brand', 'category', 'warehouse']


class VariantTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VariantType
        fields = ['id', 'name']


class VariantTypeOptionSerializer(serializers.ModelSerializer):
    variant_type = VariantTypeSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = VariantTypeOption
        fields = ['id', 'name', 'variant_type', 'created_by']


class ProductVariantSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    variant_type = VariantTypeSerializer(read_only=True, many=True)
    variant_type_option = VariantTypeOptionSerializer(read_only=True, many=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'purchase_price', 'selling_price', 'quantity', 'product', 'variant_type',
                  'variant_type_option', 'created_by']
