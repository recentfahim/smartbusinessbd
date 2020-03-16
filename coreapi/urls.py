from django.urls import path
from . import views

urlpatterns = [
    path('country/', views.GetCountry.as_view(), name='country'),
    path('city/', views.GetCity.as_view(), name='city'),
    path('company/', views.GetCompany.as_view(), name='company'),
    path('company/<int:company_id>/', views.CompanyView.as_view(), name='company_view'),
    path('image/upload/', views.ImageUpload.as_view(), name='upload_image'),
]
