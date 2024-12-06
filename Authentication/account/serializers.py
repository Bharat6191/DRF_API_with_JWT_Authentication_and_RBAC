from rest_framework import serializers
from .models import User,Project
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'role']
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username')
    class Meta:
        model=Project
        fields=['id','project_name','created_by','created_at']
