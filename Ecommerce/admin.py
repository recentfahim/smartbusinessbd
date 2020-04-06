from django.contrib import admin
from .models import EcommerceHasProduct, EcommerceSite, Partnership, SellRecord

admin.site.register(EcommerceHasProduct)
admin.site.register(EcommerceSite)
admin.site.register(Partnership)
admin.site.register(SellRecord)
