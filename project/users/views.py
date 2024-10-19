from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token


class LoginView(ModelViewSet):

    def login(self, request, *args, **kwargs):

        user = authenticate(
            username=request.data.get('email'),
            password=request.data.get('password')
        )

        if user is None:
            return Response({ 'error': 'email/password incorrect'}, status=HTTP_400_BAD_REQUEST)

        return Response(Token.objects.get(user=user).key, status=200)

