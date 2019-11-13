from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', views.GetCategory.as_view(), name='category'),
    path('country/', views.GetCountry.as_view(), name='country'),
    path('city/', views.GetCity.as_view(), name='city'),
    path('subcategory/', views.GetSubCategory.as_view(), name='subcategory'),
    path('brand/', views.GetBrand.as_view(), name='brand'),
    path('contact/company/', views.GetContactCompany.as_view(), name='contact_company'),
    path('contact/person/', views.GetContactPerson.as_view(), name='contact_company'),
    path('company/', views.GetCompany.as_view(), name='company'),
    path('partnership', views.GetPartnership.as_view(), name='partnership'),
    path('sellrecord/', views.GetSellRecord.as_view(), name='sell_record'),
    path('product/', views.GetProduct.as_view(), name='product'),
    path('category/<int:cat_id>/', views.CategoryView.as_view(), name='category_view'),
    path('subcategory/<int:sub_cat_id>/', views.SubCategoryView.as_view(), name='subcategory_view'),
    path('brand/<int:brand_id>/', views.BrandView.as_view(), name='brand_view'),
    path('contact/company/<int:contact_company_id>/', views.ContactCompanyView.as_view(), name='contact_company_view'),
    path('contact/person/<int:contact_person_id>/', views.ContactPersonView.as_view(), name='contact_person_view'),
    path('company/<int:company_id>/', views.CompanyView.as_view(), name='company_view'),
    path('partnership/<int:partnership_id>/', views.PartnershipView.as_view(), name='partnership_view'),
    path('product/<int:product_id>/', views.ProductView.as_view(), name='product_view'),
]
