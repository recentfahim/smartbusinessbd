from django.contrib import admin
from django.urls import path, include
from coreapi import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from rest_framework_jwt.settings import api_settings

if api_settings.JWT_AUTH_COOKIE:
    from rest_framework_jwt.authentication import JSONWebTokenAuthentication
    from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer
    from rest_framework_jwt.views import RefreshJSONWebToken

    RefreshJSONWebTokenSerializer._declared_fields.pop('token')

    class RefreshJSONWebTokenSerializerCookieBased(RefreshJSONWebTokenSerializer):
        def validate(self, attrs):
            if 'token' not in attrs:
                if api_settings.JWT_AUTH_COOKIE:
                    attrs['token'] = JSONWebTokenAuthentication().get_jwt_value(self.context['request'])
            return super(RefreshJSONWebTokenSerializerCookieBased, self).validate(attrs)

    RefreshJSONWebToken.serializer_class = RefreshJSONWebTokenSerializerCookieBased


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/v1/accounts/', include('allauth.urls')),
    path('api/core/v1/', include('coreapi.urls')),
    path('api/core/v1/rest-auth/', include('rest_auth.urls')),
    path('api/core/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/core/v1/rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('', views.Index.as_view(), name='home'),
    path('api/core/v1/rest-auth/google/', views.GoogleLogin.as_view(), name='google_login'),
    path('api/core/v1/', include('inventory.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)