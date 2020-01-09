from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from coreapi.components.googleviews import GoogleOAuth2AdapterIdToken
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from .models import Brand, Category, City, ContactCompany, ContactPerson, Country, CustomUser, SubCategory, Product, \
    Warehouse, Product, Partnership, Company, VariantType, ProductVariant, VariantTypeOption, SellRecord, \
    EcommerceSite, EcommerceHasProduct
from .serializers import BrandSerializer, CategorySerializer, CitySerializer, ContactCompanySerializer, \
    ContactPersonSerializer, CountrySerializer, UserSerializer, ProductSerializer, WarehouseSerializer, \
    SubCategorySerializer, CompanySerializer, PartnershipSerializer, SellRecordSerializer, EcommerceSiteSerializer, \
    EcommerceHasProductSerializer, VariantTypeSerializer, VariantTypeOptionSerializer, ProductVariantSerializer
from rest_framework.permissions import IsAuthenticated
import jwt
from django.conf import settings


class Index(TemplateView):
    template_name = 'test/index.html'


def decode_token(header):
    access_token = header.get('HTTP_AUTHORIZATION')[4:]
    print(access_token)
    decoded_access_token = jwt.decode(access_token, settings.SECRET_KEY)
    print(decoded_access_token)
    return decoded_access_token


class GetCategory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)

        context = {
            "message": "All Categories",
            "data": category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        category = Category.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            created_by=CustomUser.objects.get(pk=1)
        )
        category_serializer = CategorySerializer(category)
        context = {
            'massage': 'category created successfully',
            'data': category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetSubCategory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        sub_categories = SubCategory.objects.all()
        sub_category_serializer = SubCategorySerializer(sub_categories, many=True)

        context = {
            "message": "All Sub Categories",
            "data": sub_category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        sub_category = SubCategory.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            created_by=CustomUser.objects.get(pk=1),
            category=Category.objects.get(name=data.get('category'))
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
        city_serializer = CountrySerializer(cities, many=True)

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


class GetBrand(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        brands = Brand.objects.all()
        brand_serializer = BrandSerializer(brands, many=True)

        context = {
            'message': 'All brands',
            'data': brand_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data

        brand = Brand.objects.create(
            name=data.get('brand_name'),
            created_by=CustomUser.objects.get(username=data.get('brand_created_by')),
            logo=data.get('brand_logo'),
            url=data.get('brand_url')
        )
        brand_serializer = BrandSerializer(brand)
        context = {
            'message': 'Brand created successfully',
            'data': brand_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetContactCompany(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        companies = ContactCompany.objects.all()

        company_serializer = ContactCompanySerializer(companies, many=True)

        context = {
            'message': 'All Companies',
            'data': company_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data

        contact_company = ContactCompany.objects.create(
            company_name=data.get('company_name'),
            group_reference=data.get('group_reference'),
            attention=data.get('attention'),
            address_1=data.get('address_1'),
            address_2=data.get('address_2'),
            country=Country.objects.get(name=data.get('country')),
            city=City.objects.get(name=data.get('city')),
            post_code=data.get('post_code'),
            company_email=data.get('company_email'),
            phone=data.get('phone'),
            fax=data.get('fax'),
            mobile_number=data.get('mobile_number'),
            skype=data.get('skype'),
            website=data.get('website'),
            supplier=data.get('supplier'),
            customer=data.get('customer'),
            created_by=CustomUser.objects.get(pk=1)
        )
        contact_company_serializer = ContactCompanySerializer(contact_company)

        context = {
            'message': 'Contact Company created successfully',
            'data': contact_company_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


class GetContactPerson(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        contact_persons = ContactPerson.objects.all()

        contact_persons_serializer = ContactPersonSerializer(contact_persons, many=True)

        context = {
            'message': 'All contact persons',
            'data': contact_persons_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        contact_person = ContactPerson.objects.create(
            name=data.get('name'),
            mobile_number=data.get('mobile_number'),
            email=data.get('email'),
            supplier=data.get('is_supplier'),
            customer=data.get('is_customer'),
            company=ContactCompany.objects.filter(company_name=(data.get('company'))).first(),
            created_by=CustomUser.objects.filter(username=data.get('created_by')).first()
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
        companies = Company.objects.all()
        company_serializer = CompanySerializer(companies, many=True)

        context = {
            'message': 'All companies',
            'data': company_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        company = Company.objects.create(
            name=data.get('company_name'),
            website=data.get('company_website'),
            email=data.get('company_email'),
            address=data.get('company_address'),
            city=City.objects.get(name=data.get('company_city')),
            region=data.get('company_region'),
            postcode=data.get('company_postcode'),
            country=Country.objects.get(name=data.get('company_country')),
            phone=data.get('company_phone'),
            fax=data.get('company_fax'),
            image=data.get('company_image'),
            logo=data.get('company_logo'),
            created_by=CustomUser.objects.get(username=data.get('company_created_by')),
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
        partnership = Partnership.objects.all()
        partnership_serializer = PartnershipSerializer(partnership, many=True)

        context = {
            'message': 'All Partnerships',
            'data': partnership_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
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


class GetProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        context = {
            'message': 'All Products',
            'data': product_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
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
            sub_category=SubCategory.objects.filter(name=data.get('product_sub_category')).first(),
            warehouse=Warehouse.objects.filter(name=data.get('product_warehouse')).first(),
            company=Company.objects.filter(name=data.get('product_company')).first(),
            created_by=CustomUser.objects.filter(username=data.get('product_created_by')).first(),
        )
        product_serializer = ProductSerializer(product)
        context = {
            'message': 'Product Created Successfully',
            'data': product_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetSellRecord(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        sell_records = SellRecord.objects.all()
        sell_record_serializer = SellRecordSerializer(sell_records, many=True)
        context = {
            'message': 'All Sell Records',
            'data': sell_record_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        sell_record = SellRecord.objects.create(
            price=data.get('sell_record_price'),
            quantity=data.get('sell_record_quantity'),
            ecommerce_has_product=EcommerceHasProduct.objects.filter(pk=data.get('sell_record_store_has_product')).first(),
            created_by=CustomUser.objects.filter(username=data.get('sell_record_created_by')).first()
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
        online_stores = EcommerceSite.objects.all()
        online_stores_serializer = EcommerceSiteSerializer(online_stores, many=True)
        context = {
            'message': 'All E-commerce',
            'data': online_stores_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
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
        store_product = EcommerceHasProduct.objects.all()
        store_product_serializer = EcommerceHasProductSerializer(store_product, many=True)
        context = {
            'message': 'All Online Store has Product',
            'data': store_product_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
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


class GetVariantType(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        variant_type = VariantType.objects.all()
        variant_type_serializer = VariantTypeSerializer(variant_type, many=True)
        context = {
            'message': 'All variants',
            'data': variant_type_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        variant_type = VariantType.objects.create(
            name=data.get('variant_type_name'),
            created_by=CustomUser.objects.filter(username=data.get('variant_type_created_by')).first()
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
        variant_type_option = VariantTypeOption.objects.all()
        variant_type_option_serializer = VariantTypeOptionSerializer(variant_type_option, many=True)
        context = {
            'message': 'All variants',
            'data': variant_type_option_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        variant_type_option = VariantTypeOption.objects.create(
            name=data.get('variant_type_option_name'),
            variant_type=VariantType.objects.filter(name=data.get('variant_type')).first(),
            created_by=CustomUser.objects.filter(username=data.get('variant_type_option_created_by')).first()
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
        product_variant = ProductVariant.objects.all()
        product_variant_serializer = ProductVariantSerializer(product_variant, many=True)
        context = {
            'message': 'All Product Variants',
            'data': product_variant_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        product_variant = ProductVariant.objects.create(
            name=data.get('product_variant_name'),
            purchase_price=data.get('product_variant_purchase_price'),
            selling_price=data.get('product_variant_selling_price'),
            quantity=data.get('product_variant_quantity'),
            product=Product.objects.filter(item_name=data.get('product_variant_product')).first(),
            variant_type=VariantType.objects.filter(name=data.get('product_variant_variant_type')).first(),
            variant_type_option=VariantTypeOption.objects.filter(name=data.get('product_variant_variant_type_option').first()),
            created_by=CustomUser.objects.filter(username=data.get('product_variant_created_by')).first(),
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
        Category.objects.filter(pk=self.kwargs.get('cat_id')).update(name=name, description=description)

        category = Category.objects.get(pk=self.kwargs.get('cat_id'))
        category_serializer = CategorySerializer(category)

        context = {
            'message': 'Category updated successfully',
            'data': category_serializer.data
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
            category=Category.objects.get(name=data.get('category'))
        )
        sub_category = SubCategory.objects.filter(pk=kwargs.get('sub_cat_id'))
        sub_category_serializer = SubCategorySerializer(sub_category)
        context = {
            'massage': 'category created successfully',
            'data': sub_category_serializer.data
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


class ContactCompanyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
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
            country=Country.objects.get(name=data.get('country')),
            city=City.objects.get(name=data.get('city')),
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
        company = Company.objects.filter(pk=kwargs.get('company_id'))
        company_serializer = CompanySerializer(company)
        context = {
            'message': 'Single Company',
            'data': company_serializer.data
        }
        return Response('OK')

    def delete(self, request, *args, **kwargs):
        company = Company.objects.filter(pk=kwargs.get('company_id'))
        company.delete()
        context = {
            'message': 'Company Deleted Successfully'
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = request.data

        Company.objects.filter(pk=kwargs.get('company_id')).update(
            name=data.get('company_name'),
            website=data.get('company_website'),
            email=data.get('company_email'),
            address=data.get('company_address'),
            city=City.objects.get(name=data.get('company_city')),
            region=data.get('company_region'),
            postcode=data.get('company_postcode'),
            country=Country.objects.get(name=data.get('company_country')),
            phone=data.get('company_phone'),
            fax=data.get('company_fax'),
            image=data.get('company_image'),
            logo=data.get('company_logo'),
            updated_by=CustomUser.objects.get(username=data.get('company_created_by')),
        )
        context = {
            'message': 'Company updated successfully'
        }

        return Response(context, status=status.HTTP_200_OK)


class PartnershipView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
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


class ProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
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
            sub_category=SubCategory.objects.filter(name=data.get('product_sub_category')).first(),
            warehouse=Warehouse.objects.filter(name=data.get('product_warehouse')).first(),
            company=Company.objects.filter(name=data.get('product_company')).first(),
            updated_by=CustomUser.objects.filter(username=data.get('product_updated_by')).first(),
        )
        context = {
            'message': 'Product Updated Successfully',
        }
        return Response(context, status=status.HTTP_200_OK)


class SellRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
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


class VariantTypeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
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
        data = request.data
        VariantType.objects.filter(pk=kwargs.get('variant_type_id')).update(
            name=data.get('variant_type_name'),
            updated_by=CustomUser.objects.filter(username=data.get('variant_type_updated_by')).first()
        )
        context = {
            'message': 'Variant type updated successfully'
        }

        return Response(context, status=status.HTTP_200_OK)


class VariantTypeOptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
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
        data = request.data
        VariantTypeOption.objects.filter(pk=kwargs.get('variant_type_option_id')).update(
            name=data.get('variant_type_option_name'),
            variant_type=VariantType.objects.filter(name=data.get('variant_type')).first(),
            updated_by=CustomUser.objects.filter(username=data.get('variant_type_option_updated_by')).first()
        )
        context = {
            'message': 'Variant type option updated successfully'
        }

        return Response(context, status=status.HTTP_200_OK)


class ProductVariantView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
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
            updated_by=CustomUser.objects.filter(username=data.get('product_variant_updated_by')).first(),
        )
        context = {
            'message': 'Product Variant Updated successfully'
        }

        return Response(context, status=status.HTTP_200_OK)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2AdapterIdToken
    client_class = OAuth2Client
