from django.contrib import admin
from .models import Category, Product, ProductImage, ProductVariant, VariantType, VariantTypeOption, Brand, Warehouse

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(VariantType)
admin.site.register(VariantTypeOption)
admin.site.register(Brand)
admin.site.register(Warehouse)
