# D:\SHLOK\PhilosopherMind\users\models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields here if needed in the future
    # For now, we'll just use the default fields from AbstractUser
    # Example: is_creator = models.BooleanField(default=False)
    pass

    def __str__(self):
        return self.username