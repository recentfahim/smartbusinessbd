from django.contrib import admin
from .models import Brand, Category, City, ContactCompany, ContactPerson, Country, CustomUser, Product, SubCategory, \
    Warehouse, Partnership, Company, VariantType, ProductVariant, VariantTypeOption

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(ContactCompany)
admin.site.register(ContactPerson)
admin.site.register(Country)
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Warehouse)
admin.site.register(Partnership)
admin.site.register(Company)
admin.site.register(VariantType)
admin.site.register(ProductVariant)
admin.site.register(VariantTypeOption)
