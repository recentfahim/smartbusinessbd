from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from generic.views import decode_token
from rest_framework.response import Response
from .models import Category, Brand, Product, VariantType, VariantTypeOption, ProductVariant
from coreapi.models import Warehouse, Company
from rest_framework import status
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer, VariantTypeSerializer, \
    VariantTypeOptionSerializer, ProductVariantSerializer, CategoryCreateSerializer


class GetCategory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = decode_token(request.META)
        categories = user.category_created_by.all()
        category_serializer = CategorySerializer(categories, many=True)

        context = {
            "message": "All Categories",
            "data": category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        category = Category.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            parent=Category.objects.filter(id=data.get('parent')).first(),
            created_by=user,
        )
        category_serializer = CategorySerializer(category)
        context = {
            'massage': 'category created successfully',
            'data': category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetBrand(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        brands = user_into.brand_created_by.all()
        brand_serializer = BrandSerializer(brands, many=True)

        context = {
            'message': 'All brands',
            'data': brand_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data

        brand = Brand.objects.create(
            name=data.get('name'),
            created_by=user,
            logo=data.get('brand_logo'),
            url=data.get('brand_url')
        )
        brand_serializer = BrandSerializer(brand)
        context = {
            'message': 'Brand created successfully',
            'data': brand_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = decode_token(request.META)
        products = user.product_created_by.all()
        product_serializer = ProductSerializer(products, many=True)
        context = {
            'message': 'All Products',
            'data': product_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        product = Product.objects.create(
            item_key=data.get('product_key'),
            item_name=data.get('product_name'),
            stock_alert=data.get('product_stock_alert'),
            unit=data.get('product_unit'),
            vat=data.get('product_vat'),
            description=data.get('product_description'),
            track=data.get('product_tract'),
            brand=Brand.objects.filter(name=data.get('product_brand')).first(),
            category=Category.objects.filter(name=data.get('product_category')).first(),
            warehouse=Warehouse.objects.filter(name=data.get('product_warehouse')).first(),
            company=Company.objects.filter(name=data.get('product_company')).first(),
            created_by=user,
        )
        product_serializer = ProductSerializer(product)
        context = {
            'message': 'Product Created Successfully',
            'data': product_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetVariantType(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        variant_type = VariantType.objects.all()
        variant_type_serializer = VariantTypeSerializer(variant_type, many=True)
        context = {
            'message': 'All variants',
            'data': variant_type_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        variant_type = VariantType.objects.create(
            name=data.get('variant_type_name'),
            created_by=user
        )
        variant_type_serializer = VariantTypeSerializer(variant_type)
        context = {
            'message': 'All Variant types',
            'data': variant_type_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


class GetVariantTypeOption(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = decode_token(request.META)
        variant_type_option = user.varianttypeoption_created_by.all()
        variant_type_option_serializer = VariantTypeOptionSerializer(variant_type_option, many=True)
        context = {
            'message': 'All variants',
            'data': variant_type_option_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        variant_type_option = VariantTypeOption.objects.create(
            name=data.get('variant_type_option_name'),
            variant_type=VariantType.objects.filter(name=data.get('variant_type')).first(),
            created_by=user
        )
        variant_type_option_serializer = VariantTypeOptionSerializer(variant_type_option)
        context = {
            'message': 'All Variant Type Options',
            'data': variant_type_option_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


class GetProductVariant(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        product_variant = ProductVariant.objects.all()
        product_variant_serializer = ProductVariantSerializer(product_variant, many=True)
        context = {
            'message': 'All Product Variants',
            'data': product_variant_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        product_variant = ProductVariant.objects.create(
            name=data.get('product_variant_name'),
            purchase_price=data.get('product_variant_purchase_price'),
            selling_price=data.get('product_variant_selling_price'),
            quantity=data.get('product_variant_quantity'),
            product=Product.objects.filter(item_name=data.get('product_variant_product')).first(),
            variant_type=VariantType.objects.filter(name=data.get('product_variant_variant_type')).first(),
            variant_type_option=VariantTypeOption.objects.filter(
                name=data.get('product_variant_variant_type_option').first()),
            created_by=user
        )
        product_variant_serializer = ProductVariantSerializer(product_variant)
        context = {
            'message': 'Product Variant Created successfully',
            'data': product_variant_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reauest, *args, **kwargs):
        category = Category.objects.get(pk=self.kwargs.get('cat_id'))
        category_serializer = CategorySerializer(category)
        context = {
            'message': 'Single category',
            'data': category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        category = Category.objects.get(pk=self.kwargs.get('cat_id'))
        category.delete()
        context = {
            'message': 'category deleted successfully',
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = self.request.data
        name = data.get('name')
        description = data.get('description')
        parent = Category.objects.filter(pk=data.get('parent')).first()
        Category.objects.filter(pk=self.kwargs.get('cat_id')).update(name=name, description=description, parent=parent)

        category = Category.objects.get(pk=self.kwargs.get('cat_id'))
        category_serializer = CategorySerializer(category)

        context = {
            'message': 'Category updated successfully',
            'data': category_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


class BrandView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reauest, *args, **kwargs):
        brand = Brand.objects.get(pk=kwargs.get('brand_id'))
        brand_serializer = BrandSerializer(brand)
        context = {
            'message': 'Single Brand',
            'data': brand_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        brand = Brand.objects.get(pk=kwargs.get('brand_id'))
        brand.delete()
        context = {
            'message': 'brand deleted successfully',
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = request.data
        Brand.objects.filter(pk=kwargs.get('brand_id')).update(
            name=data.get('name'),
            logo=data.get('logo'),
            url=data.get('url')
        )
        brand = Brand.objects.get(pk=kwargs.get('brand_id'))
        brand_serializer = BrandSerializer(brand)

        context = {
            'message': 'Brand updated successfully',
            'data': brand_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


class VariantTypeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = decode_token(request.META)
        variant_type = VariantType.objects.filter(pk=kwargs.get('variant_type_id')).first()
        variant_type_serializer = VariantTypeSerializer(variant_type)
        context = {
            'message': 'Single Variant Type',
            'data': variant_type_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        variant_type = VariantType.objects.filter(pk=kwargs.get('variant_type_id')).first()
        variant_type.delete()
        context = {
            'message': 'Variant type deleted successfully'
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        VariantType.objects.filter(pk=kwargs.get('variant_type_id')).update(
            name=data.get('variant_type_name'),
            updated_by=user
        )
        context = {
            'message': 'Variant type updated successfully'
        }

        return Response(context, status=status.HTTP_200_OK)


class VariantTypeOptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        variant_type_option = VariantTypeOption.objects.filter(pk=kwargs.get('variant_type_option_id')).first()
        variant_type_option_serializer = VariantTypeOptionSerializer(variant_type_option)
        context = {
            'message': 'Single Variant Type Option',
            'data': variant_type_option_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        variant_type_option = VariantTypeOption.objects.filter(pk=kwargs.get('variant_type_option_id')).first()
        variant_type_option.delete()
        context = {
            'message': 'Variant type option deleted successfully'
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        VariantTypeOption.objects.filter(pk=kwargs.get('variant_type_option_id')).update(
            name=data.get('variant_type_option_name'),
            variant_type=VariantType.objects.filter(name=data.get('variant_type')).first(),
            updated_by=user
        )
        context = {
            'message': 'Variant type option updated successfully'
        }

        return Response(context, status=status.HTTP_200_OK)


class ProductVariantView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = decode_token(request.META)
        product_variant = ProductVariant.objects.filter(pk=kwargs.get('product_variant_id')).first()
        product_variant_serializer = ProductVariantSerializer(product_variant)
        context = {
            'message': 'Single Product Variant',
            'data': product_variant_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        product_variant = ProductVariant.objects.filter(pk=kwargs.get('product_variant_id')).first()
        product_variant.delete()
        context = {
            'message': 'Product Variant Deleted Successfully',
        }

        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        ProductVariant.objects.filter(pk=kwargs.get('product_variant_id')).update(
            name=data.get('product_variant_name'),
            purchase_price=data.get('product_variant_purchase_price'),
            selling_price=data.get('product_variant_selling_price'),
            quantity=data.get('product_variant_quantity'),
            product=Product.objects.filter(item_name=data.get('product_variant_product')).first(),
            variant_type=VariantType.objects.filter(name=data.get('product_variant_variant_type')).first(),
            variant_type_option=VariantTypeOption.objects.filter(
                name=data.get('product_variant_variant_type_option').first()),
            updated_by=user
        )
        context = {
            'message': 'Product Variant Updated successfully'
        }

        return Response(context, status=status.HTTP_200_OK)


class ProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        product = Product.objects.filter(pk=kwargs.get('product_id')).first()
        product_serializer = ProductSerializer(product)
        context = {
            'message': 'Single products',
            'data': product_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        product = Product.objects.filter(pk=kwargs.get('product_id')).first()
        product.delete()
        context = {
            'message': 'Product delete successfully'
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        product = Product.objects.filter(pk=kwargs.get('product_id')).update(
            item_key=data.get('product_key'),
            item_name=data.get('product_name'),
            stock_alert=data.get('product_stock_alert'),
            unit=data.get('product_unit'),
            vat=data.get('product_vat'),
            description=data.get('product_description'),
            track=data.get('product_tract'),
            brand=Brand.objects.filter(name=data.get('product_brand')).first(),
            category=Category.objects.filter(name=data.get('product_category')).first(),
            warehouse=Warehouse.objects.filter(name=data.get('product_warehouse')).first(),
            company=Company.objects.filter(name=data.get('product_company')).first(),
            updated_by=user,
        )
        context = {
            'message': 'Product Updated Successfully',
        }
        return Response(context, status=status.HTTP_200_OK)
