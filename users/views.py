from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from users.components.googleviews import GoogleOAuth2AdapterIdToken
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2AdapterIdToken
    client_class = OAuth2Client