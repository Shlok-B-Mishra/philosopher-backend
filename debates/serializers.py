# debates/serializers.py

from rest_framework import serializers
from .models import Debate
from users.models import CustomUser

# A simple serializer to represent the creator's username
class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']

class DebateSerializer(serializers.ModelSerializer):
    # We replace the creator's ID with more useful info (username)
    # read_only=True means we can't set the creator through this nested serializer
    creator = CreatorSerializer(read_only=True)

    class Meta:
        model = Debate
        # List all the fields you want to expose in your API
        fields = [
            'id',
            'title',
            'description',
            'creator', # This will now use the CreatorSerializer
            'livepeer_embed_url', # <-- ADD THIS
            'status',
            'scheduled_start_time',
            'created_at',
        ]