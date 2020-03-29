from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from .models import City, Country, Company
from .serializers import CitySerializer, CountrySerializer, CompanySerializer
from rest_framework.permissions import IsAuthenticated
import string
import random
import os
from generic.views import decode_token


class Index(TemplateView):
    template_name = 'test/index.html'


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


class ImageUpload(APIView):
    permission_classes = [IsAuthenticated]

    def handle_uploaded_file(self, file):
        file_name = file.name
        char = string.ascii_letters
        cover_string = ''.join(random.choice(char) for x in range(36))
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        folder = os.path.join(path, 'media', 'images')

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
