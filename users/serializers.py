# users/serializers.py

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # We only expose non-sensitive fields
        fields = ['id', 'username', 'first_name', 'last_name']