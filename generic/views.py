from django.shortcuts import render
from django.conf import settings
import jwt
from users.models import User


def decode_token(header):
    access_token = header.get('HTTP_AUTHORIZATION')[4:]
    decoded_access_token = jwt.decode(access_token, settings.SECRET_KEY)
    user = User.objects.filter(pk=decoded_access_token.get('user_id')).first()

    return user
