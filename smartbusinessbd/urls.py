from django.contrib import admin
from django.urls import path, include
from coreapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/v1/accounts/', include('allauth.urls')),
    path('api/core/v1/', include('coreapi.urls')),
    path('api/core/v1/rest-auth/', include('rest_auth.urls')),
    path('api/core/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/core/v1/rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('', views.Index.as_view(), name='home'),
]
