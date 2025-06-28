from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth.models import User

# Sustituye con tu Client ID real
GOOGLE_CLIENT_ID = '749356252141-i34hh87haambamufa1ediieospcpptif.apps.googleusercontent.com'

class GoogleTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split(' ')[1]

        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        except Exception:
            raise AuthenticationFailed('Token de Google inválido o expirado.')

        email = idinfo.get('email')
        if not email:
            raise AuthenticationFailed('Token válido pero sin email.')

        user, _ = User.objects.get_or_create(username=email, defaults={'email': email})
        return (user, None)