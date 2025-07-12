# users/views.py

from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

# This view handles listing all users
class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# This view handles retrieving a single user by their ID
class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer