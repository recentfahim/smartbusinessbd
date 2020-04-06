from django.urls import path
from .views import PartnershipView, GetPartnership, GetOnlineSore, OnlineStoreView, GetOnlineStoreHasProduct, \
    OnlineStoreHasProductView, GetSellRecord, SellRecordView

urlpatterns = [
    path('Ecommerce/', GetPartnership.as_view(), name='Ecommerce'),
    path('sell_record/', GetSellRecord.as_view(), name='sell_record'),
    path('e-commerce/', GetOnlineSore.as_view(), name='e_commerce'),
    path('e-commerce_product/', GetOnlineStoreHasProduct.as_view(), name='e_commerce_product'),
    path('Ecommerce/<int:partnership_id>/', PartnershipView.as_view(), name='partnership_view'),
    path('sell_record/<int:sell_record_id>/', SellRecordView.as_view(), name='sell_record_view'),
    path('e-commerce/<int:e_commerce_id>/', OnlineStoreView.as_view(), name='e_commerce_view'),
    path('e-commerce_product/<int:e_commerce_has_product_id>/', OnlineStoreHasProductView.as_view(),
         name='e_commerce_product_view'),
]
