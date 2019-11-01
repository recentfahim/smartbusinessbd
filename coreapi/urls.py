from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', views.GetCategory.as_view(), name='category'),
    path('country/', views.GetCountry.as_view(), name='country'),
    path('city/', views.GetCity.as_view(), name='city'),
    path('subcategory/', views.GetSubCategory.as_view(), name='subcategory'),
    path('brand/', views.GetBrand.as_view(), name='brand'),
]
