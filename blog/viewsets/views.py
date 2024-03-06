# we will be using this viewsets for users operations

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from blog.viewsets.serializer import UserSerializer

User = get_user_model()

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #print(queryset)
