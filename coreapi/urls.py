from django.urls import path
from . import views

urlpatterns = [
    path('country/', views.GetCountry.as_view(), name='country'),
    path('city/', views.GetCity.as_view(), name='city'),
    path('subcategory/', views.GetSubCategory.as_view(), name='subcategory'),
    path('contact/company/', views.GetContactCompany.as_view(), name='contact_company'),
    path('contact/person/', views.GetContactPerson.as_view(), name='contact_company'),
    path('company/', views.GetCompany.as_view(), name='company'),
    path('partnership/', views.GetPartnership.as_view(), name='partnership'),
    path('sell_record/', views.GetSellRecord.as_view(), name='sell_record'),
    path('e-commerce/', views.GetOnlineSore.as_view(), name='e_commerce'),
    path('e-commerce_product/', views.GetOnlineStoreHasProduct.as_view(), name='e_commerce_product'),

    path('contact/company/<int:contact_company_id>/', views.ContactCompanyView.as_view(), name='contact_company_view'),
    path('contact/person/<int:contact_person_id>/', views.ContactPersonView.as_view(), name='contact_person_view'),
    path('company/<int:company_id>/', views.CompanyView.as_view(), name='company_view'),
    path('partnership/<int:partnership_id>/', views.PartnershipView.as_view(), name='partnership_view'),
    path('product/<int:product_id>/', views.ProductView.as_view(), name='product_view'),
    path('sell_record/<int:sell_record_id>/', views.SellRecordView.as_view(), name='sell_record_view'),
    path('e-commerce/<int:e_commerce_id>/', views.OnlineStoreView.as_view(), name='e_commerce_view'),
    path('e-commerce_product/<int:e_commerce_has_product_id>/', views.OnlineStoreHasProductView.as_view(), name='e_commerce_product_view'),

    path('image/upload/', views.ImageUpload.as_view(), name='upload_image'),
]
