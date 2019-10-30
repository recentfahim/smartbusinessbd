from django.contrib import admin
from .models import City, Country, ContactCompany

admin.site.register(City)
admin.site.register(Country)
admin.site.register(ContactCompany)
