from django.urls import path
from .views import GetCategory, GetProduct, GetBrand, GetVariantType, GetProductVariant, GetVariantTypeOption, \
    CategoryView, BrandView, VariantTypeView, VariantTypeOptionView, ProductVariantView, ProductView, GetWarehouse, \
    WarehouseView

urlpatterns = [
    path('category/', GetCategory.as_view(), name='category'),
    path('product/', GetProduct.as_view(), name='product'),
    path('brand/', GetBrand.as_view(), name='brand'),
    path('variant_type/', GetVariantType.as_view(), name='variant_type'),
    path('variant_type_option/', GetVariantTypeOption.as_view(), name='variant_type_option'),
    path('product_variant/', GetProductVariant.as_view(), name='product_variant'),
    path('category/<int:cat_id>/', CategoryView.as_view(), name='category_view'),
    path('brand/<int:brand_id>/', BrandView.as_view(), name='brand_view'),
    path('variant_type/<int:variant_type_id>/', VariantTypeView.as_view(), name='variant_type_view'),
    path('variant_type_option/<int:variant_type_option_id>/', VariantTypeOptionView.as_view(),
         name='variant_type_option_view'),
    path('product_variant/<int:product_variant>/', ProductVariantView.as_view(), name='product_variant_view'),
    path('product/<int:product_id>/', ProductView.as_view(), name='product_view'),
    path('warehouse/', GetWarehouse.as_view(), name='warehouse'),
    path('warehouse/<int:warehouse_id>/', WarehouseView.as_view(), name='warehouse_view'),

]
