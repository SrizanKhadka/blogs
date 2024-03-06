from rest_framework import serializers
from authentication.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    
    class Meta:
        model = UserModel
        fields = ["username","email","password"]
    