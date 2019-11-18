from django.contrib import admin
from django.urls import path, include
from coreapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/core/v1/', include('coreapi.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('', views.Index.as_view(), name='home'),
]
