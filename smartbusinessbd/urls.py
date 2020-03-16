from django.contrib import admin
from django.urls import path, include
from coreapi import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/v1/accounts/', include('allauth.urls')),
    path('api/core/v1/', include('coreapi.urls')),
    path('', views.Index.as_view(), name='home'),
    path('api/core/v1/', include('inventory.urls')),
    path('api/core/v1/users/', include('users.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
