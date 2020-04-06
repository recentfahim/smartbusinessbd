from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from generic.views import decode_token
from .models import Partnership, EcommerceSite, EcommerceHasProduct, SellRecord
from .serializers import EcommerceHasProductSerializer, PartnershipSerializer, EcommerceSiteSerializer, \
    SellRecordSerializer
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from inventory.models import Product
from inventory.serializers import ProductSerializer
from coreapi.models import Company


class GetPartnership(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        partnership = Partnership.objects.all()
        partnership_serializer = PartnershipSerializer(partnership, many=True)

        context = {
            'message': 'All Partnerships',
            'data': partnership_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data

        partner = Partnership.objects.create(
            partner=User.objects.filter(username=data.get('partner_username')).first(),
            company=Company.objects.filter(name=data.get('partner_company')).first(),
            product=Product.objects.filter(item_name=data.get('partner_product')).first(),
            percentage=data.get('partnership_percentage'),
            created_by=user
        )
        partner_serializer = PartnershipSerializer(partner)
        context = {
            'message': 'Partner created successfully',
            'data': partner_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)



class GetSellRecord(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        sell_records = SellRecord.objects.all()
        sell_record_serializer = SellRecordSerializer(sell_records, many=True)
        context = {
            'message': 'All Sell Records',
            'data': sell_record_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        data = request.data
        sell_record = SellRecord.objects.create(
            price=data.get('sell_record_price'),
            quantity=data.get('sell_record_quantity'),
            ecommerce_has_product=EcommerceHasProduct.objects.filter(pk=data.get('sell_record_store_has_product')).first(),
            created_by=user_into
        )
        sell_record_serializer = SellRecordSerializer(sell_record)
        context = {
            'message': 'Sell Record Created Successfully',
            'data': sell_record_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)



class GetOnlineSore(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        online_stores = EcommerceSite.objects.all()
        online_stores_serializer = EcommerceSiteSerializer(online_stores, many=True)
        context = {
            'message': 'All E-commerce',
            'data': online_stores_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        online_store = EcommerceSite.objects.create(
            name=data.get('online_store_name'),
            logo=data.get('online_store_logo_path'),
            website=data.get('online_store_website'),
            shop_link=data.get('online_store_shop_link'),
            created_by=user
        )
        online_store_serializer = EcommerceSiteSerializer(online_store)
        context = {
            'message': 'E-commerce Created Successfully',
            'data': online_store_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetOnlineStoreHasProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        store_product = EcommerceHasProduct.objects.all()
        store_product_serializer = EcommerceHasProductSerializer(store_product, many=True)
        context = {
            'message': 'All Online Store has Product',
            'data': store_product_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        store_product = EcommerceHasProduct.objects.create(
            price=data.get('store_product_price'),
            quantity=data.get('store_product_quantity'),
            product=Product.objects.filter(item_name=data.get('store_product_product')).first(),
            ecommerce=EcommerceSite.objects.filter(name=data.get('store_product_e_commerce')).first(),
            created_by=user,
        )
        store_product_serializer = EcommerceHasProductSerializer(store_product)
        context = {
            'message': 'Online store has product created successfully',
            'data': store_product_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)



class PartnershipView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = decode_token(request.META)
        partner = Partnership.objects.filter(pk=kwargs.get('partnership_id')).first()
        partner_serializer = PartnershipSerializer(partner)
        context = {
            'message': 'Single Partners',
            'data': partner_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        partner = Partnership.objects.filter(pk=kwargs.get('partnership_id'))
        partner.delete()
        context = {
            'message': 'Partner Deleted Successfully'
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        partner = Partnership.objects.filter(pk=kwargs.get('partnership_id')).update(
            partner=User.objects.filter(username=data.get('partner_username')).first(),
            company=Company.objects.filter(name=data.get('partner_company')).first(),
            product=Product.objects.filter(item_name=data.get('partner_product')).first(),
            percentage=data.get('partnership_percentage'),
            updated_by=user,
        )
        context = {
            'message': 'Partner updated successfully',
        }
        return Response(context, status=status.HTTP_200_OK)



class SellRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        sell_record = SellRecord.objects.filter(pk=kwargs.get('sell_record_id'))
        sell_record_serializer = ProductSerializer(sell_record)
        context = {
            'message': 'Single Sell Record',
            'data': sell_record_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        sell_record = SellRecord.objects.filter(pk=kwargs.get('sell_record_id'))
        sell_record.delete()
        context = {
            'message': 'Sell Record delete successfully'
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = request.data
        sell_record = SellRecord.objects.filter(pk=kwargs.get('sell_record_id')).update(
            price=data.get('sell_record_price'),
            quantity=data.get('sell_record_quantity'),
            ecommerce_has_product=data.get('sell_record_store_has_product'),
            updated_by=data.get('sell_record_updated_by')
        )
        context = {
            'message': 'Sell Record updated successfully'
        }
        return Response(context, status=status.HTTP_200_OK)


class OnlineStoreView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        online_store = EcommerceSite.objects.filter(pk=kwargs.get('e_commerce_id')).first()
        online_store_serializer = EcommerceSiteSerializer(online_store)
        context = {
            'message': 'Single E-commerce',
            'data': online_store_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        online_store = EcommerceSite.objects.filter(pk=kwargs.get('e_commerce_id')).first()
        online_store.delete()
        context = {
            'message': 'E-commerce Deleted Successfully'
        }

        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        EcommerceSite.objects.filter(pk=kwargs.get('e_commerce_id')).update(
            name=data.get('online_store_name'),
            logo=data.get('online_store_logo_path'),
            website=data.get('online_store_website'),
            shop_link=data.get('online_store_shop_link'),
            updated_by=user,
        )
        context = {
            'message': 'E-commerce Updated Successfully',
        }

        return Response(context, status=status.HTTP_200_OK)


class OnlineStoreHasProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        store_has_product = EcommerceSite.objects.filter(pk=kwargs.get('e_commerce_has_product_id')).first()
        store_has_product_serializer = EcommerceHasProductSerializer(store_has_product)
        context = {
            'message': 'Single Online Store has Product',
            'data': store_has_product_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        store_has_product = EcommerceSite.objects.filter(pk=kwargs.get('e_commerce_has_product_id'))
        store_has_product.delete()
        context = {
            'message': 'Online Store has Product deleted successfully',
        }

        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = decode_token(request.META)
        data = request.data
        store_product = EcommerceHasProduct.objects.filter(pk=kwargs.get('e_commerce_has_product_id')).update(
            price=data.get('store_product_price'),
            quantity=data.get('store_product_quantity'),
            product=Product.objects.filter(item_name=data.get('store_product_product')).first(),
            ecommerce=EcommerceSite.objects.filter(name=data.get('store_product_e_commerce')).first(),
            updated_by=user,
        )
        context = {
            'message': 'Online Store has product updated successfully',
        }

        return Response(context, status=status.HTTP_200_OK)
