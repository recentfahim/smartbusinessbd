from django.contrib import admin
from .models import EcommerceHasProduct, EcommerceSite, Partnership, SellRecord, StoreProduct, \
    StoreProductTransaction, ProductTransaction


admin.site.register(EcommerceHasProduct)
admin.site.register(EcommerceSite)
admin.site.register(Partnership)
admin.site.register(SellRecord)
admin.site.register(StoreProduct)
admin.site.register(StoreProductTransaction)
admin.site.register(ProductTransaction)
