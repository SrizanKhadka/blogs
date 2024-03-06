from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from authentication.api.serializer import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LoginAPIView(APIView):

    def post(self, request):
        user = authenticate(
            username=request.data["username"], password=request.data["password"]
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"error": "Invalid credentials"}, status=401)


'''
 This is tuple unpacking. The result of Token.objects.get_or_create(user=user) is a tuple containing two values: 
 the token object and a boolean indicating whether the token was created (True) or already existed (False). 
 
 So, after this line executes:

token will hold the Token object (either existing or newly created).
created will be a boolean indicating whether the token was just created (True) or already existed (False).
'''