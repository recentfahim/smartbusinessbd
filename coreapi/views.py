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
