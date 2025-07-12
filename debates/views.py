# debates/views.py

from rest_framework import generics
from .models import Debate
from .serializers import DebateSerializer

# This view handles listing all debates (GET) and creating a new debate (POST)
class DebateList(generics.ListCreateAPIView):
    queryset = Debate.objects.all().order_by('-scheduled_start_time') # Get all debates, newest first
    serializer_class = DebateSerializer

# This view handles retrieving (GET), updating (PUT), and deleting (DELETE) a single debate
class DebateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer