from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from coreapi.components.googleviews import GoogleOAuth2AdapterIdToken
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from .models import City, Country, Warehouse, Company
from inventory.models import Brand, Category, Product, VariantType, ProductVariant, VariantTypeOption
from users.models import User
from partnership.models import Partnership, EcommerceHasProduct, EcommerceSite, SellRecord
from .serializers import CitySerializer, ContactCompanySerializer, CountrySerializer, CompanySerializer
from rest_framework.permissions import IsAuthenticated
import jwt
from django.conf import settings
import string
import random
import os


class Index(TemplateView):
    template_name = 'test/index.html'





class GetSubCategory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print(request.META)
        user_into = decode_token(request.META)
        sub_categories = user_into.sub_category_created_by.all()
        sub_category_serializer = SubCategorySerializer(sub_categories, many=True)

        context = {
            "message": "All Sub Categories",
            "data": sub_category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        data = request.data
        sub_category = SubCategory.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            created_by=user_into,
            category=Category.objects.get(pk=data.get('category'))
        )
        sub_category_serializer = SubCategorySerializer(sub_category)
        context = {
            'massage': 'category created successfully',
            'data': sub_category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetCountry(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        countries = Country.objects.all()
        country_serializer = CountrySerializer(countries, many=True)

        context = {
            'message': 'All countries',
            'data': country_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data

        country = Country.objects.create(
            name=data.get('name')
        )
        country_serializer = CountrySerializer(country)
        context = {
            'message': 'Country created successfully',
            'data': country_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetCity(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cities = City.objects.all()
        city_serializer = CitySerializer(cities, many=True)

        context = {
            'message': 'All cities',
            'data': city_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data

        city = City.objects.create(
            name=data.get('name'),
            country=Country.objects.get(name=data.get('country'))
        )
        city_serializer = CitySerializer(city)
        context = {
            'message': 'City created successfully',
            'data': city_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)



class GetContactCompany(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        companies = user_into.contact_company_created_by.all()

        company_serializer = ContactCompanySerializer(companies, many=True)

        context = {
            'message': 'All Companies',
            'data': company_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        data = request.data

        contact_company = ContactCompany.objects.create(
            company_name=data.get('company_name'),
            group_reference=data.get('group_reference'),
            attention=data.get('attention'),
            address_1=data.get('address_1'),
            address_2=data.get('address_2'),
            country=Country.objects.get(pk=data.get('country')),
            city=City.objects.get(pk=data.get('city')),
            post_code=data.get('post_code'),
            company_email=data.get('company_email'),
            phone=data.get('phone'),
            fax=data.get('fax'),
            mobile_number=data.get('mobile_number'),
            skype=data.get('skype'),
            website=data.get('website'),
            supplier=data.get('supplier'),
            customer=data.get('customer'),
            created_by=user_into,
        )
        contact_company_serializer = ContactCompanySerializer(contact_company)

        context = {
            'message': 'Contact Company created successfully',
            'data': contact_company_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


class GetContactPerson(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        contact_persons = user_into.contact_person_created_by.all()

        contact_persons_serializer = ContactPersonSerializer(contact_persons, many=True)

        context = {
            'message': 'All contact persons',
            'data': contact_persons_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        data = request.data

        contact_person = ContactPerson.objects.create(
            name=data.get('name'),
            mobile_number=data.get('mobile_number'),
            email=data.get('email'),
            supplier=data.get('is_supplier'),
            customer=data.get('is_customer'),
            company=ContactCompany.objects.filter(company_name=(data.get('company'))).first(),
            created_by=user_into,
        )

        contact_person_serializer = ContactPersonSerializer(contact_person)

        context = {
            'message': 'Contact person saved successfully',
            'data': contact_person_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetCompany(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        companies = user_into.company_created_by.all()
        company_serializer = CompanySerializer(companies, many=True)

        context = {
            'message': 'All companies',
            'data': company_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        data = request.data
        print(data)
        company = Company.objects.create(
            name=data.get('name'),
            website=data.get('website'),
            email=data.get('email'),
            address=data.get('address'),
            city=City.objects.get(pk=data.get('city')),
            region=data.get('region'),
            postcode=data.get('postcode'),
            country= Country.objects.get(pk=data.get('country')),
            phone=data.get('phone'),
            fax=data.get('fax'),
            image=data.get('image'),
            logo=data.get('logo'),
            created_by=user_into,
        )
        company_serializer = CompanySerializer(company)
        context = {
            'message': 'Company Created Successfully',
            'data': company_serializer.data

        }
        return Response(context, status=status.HTTP_200_OK)


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
        user_into = decode_token(request.META)
        data = request.data

        partner = Partnership.objects.create(
            partner=CustomUser.objects.filter(username=data.get('partner_username')).first(),
            company=Company.objects.filter(name=data.get('partner_company')).first(),
            product=Product.objects.filter(item_name=data.get('partner_product')).first(),
            percentage=data.get('partnership_percentage'),
            created_by=CustomUser.objects.filter(username=data.get('partner_created_by')).first()
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
        user_into = decode_token(request.META)
        data = request.data
        online_store = EcommerceSite.objects.create(
            name=data.get('online_store_name'),
            logo=data.get('online_store_logo_path'),
            website=data.get('online_store_website'),
            shop_link=data.get('online_store_shop_link'),
            created_by=CustomUser.objects.filter(username=data.get('online_store_created_by')).first(),
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
        user_into = decode_token(request.META)
        data = request.data
        store_product = EcommerceHasProduct.objects.create(
            price=data.get('store_product_price'),
            quantity=data.get('store_product_quantity'),
            product=Product.objects.filter(item_name=data.get('store_product_product')).first(),
            ecommerce=EcommerceSite.objects.filter(name=data.get('store_product_e_commerce')).first(),
            created_by=CustomUser.objects.filter(username=data.get('store_product_created_by')).first(),
        )
        store_product_serializer = EcommerceHasProductSerializer(store_product)
        context = {
            'message': 'Online store has product created successfully',
            'data': store_product_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)



class SubCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reauest, *args, **kwargs):
        sub_category = SubCategory.objects.get(pk=kwargs.get('sub_cat_id'))
        sub_category_serializer = SubCategorySerializer(sub_category)
        context = {
            'message': 'Single category',
            'data': sub_category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        sub_category = SubCategory.objects.get(pk=kwargs.get('sub_cat_id'))
        sub_category.delete()
        context = {
            'message': 'sub category deleted successfully',
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = request.data
        sub_category = SubCategory.objects.filter(pk=kwargs.get('sub_cat_id')).update(
            name=data.get('name'),
            description=data.get('description'),
            category=Category.objects.get(pk=data.get('category'))
        )
        sub_category = SubCategory.objects.filter(pk=kwargs.get('sub_cat_id'))
        sub_category_serializer = SubCategorySerializer(sub_category)
        context = {
            'massage': 'category created successfully',
            'data': sub_category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)



class ContactCompanyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        contact_company = ContactCompany.objects.get(pk=kwargs.get('contact_company_id'))
        contact_company_serializer = ContactCompanySerializer(contact_company)
        context = {
            'message': 'Single Contact company',
            'data': contact_company_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        contact_company = ContactCompany.objects.get(pk=kwargs.get('contact_company_id'))
        contact_company.delete()

        context = {
            'message': 'Contact company deleted successfully'
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = request.data
        ContactCompany.objects.filter(pk=kwargs.get('contact_company_id')).update(
            company_name=data.get('company_name'),
            group_reference=data.get('group_reference'),
            attention=data.get('attention'),
            address_1=data.get('address_1'),
            address_2=data.get('address_2'),
            country=Country.objects.get(pk=data.get('country')),
            city=City.objects.get(pk=data.get('city')),
            post_code=data.get('post_code'),
            company_email=data.get('company_email'),
            phone=data.get('phone'),
            fax=data.get('fax'),
            mobile_number=data.get('mobile_number'),
            skype=data.get('skype'),
            website=data.get('website'),
            supplier=data.get('supplier'),
            customer=data.get('customer'),
        )
        contact_company = ContactCompany.objects.get(pk=kwargs.get('contact_company_id'))
        contact_company_serializer = ContactCompanySerializer(contact_company)

        context = {
            'message': 'Contact company updated successfully',
            'data': contact_company_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


class ContactPersonView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        contact_person = ContactPerson.objects.filter(pk=kwargs.get('contact_person_id')).first()
        contact_person_serializer = ContactPersonSerializer(contact_person)

        context = {
            'message': 'Single Contact Person',
            'data': contact_person_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        contact_person = ContactPerson.objects.filter(pk=kwargs.get('contact_person_id')).first()
        contact_person.delete()
        context = {
            'message': 'Single Contact Person deleted successfully'
        }

        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = request.data
        contact_person = ContactPerson.objects.filter(pk=kwargs.get('contact_person_id')).update(
            name=data.get('name'),
            mobile_number=data.get('mobile_number'),
            email=data.get('email'),
            supplier=data.get('is_supplier'),
            customer=data.get('is_customer'),
            company=ContactCompany.objects.filter(company_name=(data.get('company'))).first(),
            updated_by=CustomUser.objects.filter(username=data.get('updated_by')).first()
        )

        contact_person_serializer = ContactPersonSerializer(contact_person)

        context = {
            'message': 'Contact person updated successfully',
            'data': contact_person_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class CompanyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
        company = Company.objects.get(pk=kwargs.get('company_id'))
        company_serializer = CompanySerializer(company)
        context = {
            'message': 'Single Company',
            'data': company_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        company = Company.objects.get(pk=kwargs.get('company_id'))
        company.delete()
        context = {
            'message': 'Company Deleted Successfully'
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = request.data

        Company.objects.filter(pk=kwargs.get('company_id')).update(
            name=data.get('name'),
            website=data.get('website'),
            email=data.get('email'),
            address=data.get('address'),
            city=City.objects.get(pk=data.get('city')),
            region=data.get('region'),
            postcode=data.get('postcode'),
            country=Country.objects.get(pk=data.get('country')),
            phone=data.get('phone'),
            fax=data.get('fax'),
            image=data.get('image'),
            logo=data.get('logo'),
          #  updated_by=CustomUser.objects.get(username=data.get('created_by')),
        )
        context = {
            'message': 'Company updated successfully'
        }

        return Response(context, status=status.HTTP_200_OK)


class PartnershipView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_into = decode_token(request.META)
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
        data = request.data
        partner = Partnership.objects.filter(pk=kwargs.get('partnership_id')).update(
            partner=CustomUser.objects.filter(username=data.get('partner_username')).first(),
            company=Company.objects.filter(name=data.get('partner_company')).first(),
            product=Product.objects.filter(item_name=data.get('partner_product')).first(),
            percentage=data.get('partnership_percentage'),
            updated_by=CustomUser.objects.filter(username=data.get('partner_created_by')).first()
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
        data = request.data
        EcommerceSite.objects.filter(pk=kwargs.get('e_commerce_id')).update(
            name=data.get('online_store_name'),
            logo=data.get('online_store_logo_path'),
            website=data.get('online_store_website'),
            shop_link=data.get('online_store_shop_link'),
            updated_by=CustomUser.objects.filter(username=data.get('online_store_updated_by')).first(),
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
        data = request.data
        store_product = EcommerceHasProduct.objects.filter(pk=kwargs.get('e_commerce_has_product_id')).update(
            price=data.get('store_product_price'),
            quantity=data.get('store_product_quantity'),
            product=Product.objects.filter(item_name=data.get('store_product_product')).first(),
            ecommerce=EcommerceSite.objects.filter(name=data.get('store_product_e_commerce')).first(),
            updated_by=CustomUser.objects.filter(username=data.get('store_product_updated_by')).first(),
        )
        context = {
            'message': 'Online Store has product updated successfully',
        }

        return Response(context, status=status.HTTP_200_OK)



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2AdapterIdToken
    client_class = OAuth2Client


class ImageUpload(APIView):
    permission_classes = [IsAuthenticated]

    def handle_uploaded_file(self, file):
        file_name = file.name
        char = string.ascii_letters
        cover_string = ''.join(random.choice(char) for x in range(36))
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        folder = os.path.join(path, '../../../media', 'images')

        if not os.path.exists(path):
            os.makedirs(folder, exist_ok=True)

        new_file_name = cover_string + '.' + file_name.split('.')[-1]
        photo = os.path.join(folder, new_file_name)
        with open(photo, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return new_file_name

    def post(self, request, *args, **kwargs):
        req = request.data
        image_path = self.handle_uploaded_file(req.get('file'))
        context = {
            'message': 'Image uploaded successfully',
            'path': image_path,
        }

        return Response({'data': context}, status=status.HTTP_200_OK)
