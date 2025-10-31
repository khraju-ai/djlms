from rest_framework import serializers
from django.contrib.auth import get_user_model

#create your serializers 

User = get_user_model()

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username','email','password','role']
        
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user