# we will be using this viewsets for users operations

#from django.contrib.auth.models import User
from authentication.models import UserModel
from rest_framework import viewsets
from blog.viewsets.serializer import UserSerializer

class UserViewSets(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    #print(queryset)
