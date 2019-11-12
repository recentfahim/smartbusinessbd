from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Brand, Category, City, ContactCompany, ContactPerson, Country, CustomUser, SubCategory, Product, \
    Warehouse
from .serializers import BrandSerializer, CategorySerializer, CitySerializer, ContactCompanySerializer, ContactPersonSerializer, \
    CountrySerializer, CustomUserSerializer, ProductSerializer, WarehouseSerializer, SubCategorySerializer


class GetCategory(APIView):
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
        category = Category.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            user=CustomUser.objects.get(pk=1)
        )
        category_serializer = CategorySerializer(category)
        context = {
            'massage': 'category created successfully',
            'data': category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetSubCategory(APIView):
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
            user=CustomUser.objects.get(pk=1),
            category=Category.objects.get(name=data.get('category'))
        )
        sub_category_serializer = SubCategorySerializer(sub_category)
        context = {
            'massage': 'category created successfully',
            'data': sub_category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetCountry(APIView):
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
            name=data.get('name'),
            user=CustomUser.objects.get(pk=1),
            logo=data.get('logo'),
            url=data.get('url')
        )
        brand_serializer = BrandSerializer(brand)
        context = {
            'message': 'Brand created successfully',
            'data': brand_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


class GetContactCompany(APIView):
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
            user=CustomUser.objects.get(pk=1)
        )
        contact_company_serializer = ContactCompanySerializer(contact_company)

        context = {
            'message': 'Contact Company created successfully',
            'data': contact_company_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


class GetContactPerson(APIView):
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


class CategoryView(APIView):
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
