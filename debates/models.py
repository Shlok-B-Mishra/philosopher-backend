# debates/models.py

from django.db import models
from django.conf import settings # Important for linking to our CustomUser model

class Debate(models.Model):
    # We use an Enum for the status to avoid magic strings
    class Status(models.TextChoices):
        UPCOMING = 'UP', 'Upcoming'
        LIVE = 'LI', 'Live'
        PAST = 'PA', 'Past'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Link to the user who created this debate
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, # If a user is deleted, their debates are also deleted
        related_name='debates'
    )
    # This will hold the Livepeer playback URL
    livepeer_embed_url = models.URLField(max_length=255, blank=True)
    # Status of the debate
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.UPCOMING
    )
    # Timestamps
    scheduled_start_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title