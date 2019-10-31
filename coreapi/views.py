from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Brand, Category, City, ContactCompany, ContactPerson, Country, CustomUser, SubCategory, Product, \
    Warehouse
from .serializers import BrandSerializer, CategorySerializer, CitySerializer, ContactCompanySerializer, ContactPersonSerializer, \
    CountrySerializer, CustomUserSerializer, ProductSerializer, WarehouseSerializer


class GetCategory(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        
        category_serializer = CategorySerializer(categories, many=True)

        context = {
            "message": "Categories",
            "data": category_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)
