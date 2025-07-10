# debates/admin.py

from django.contrib import admin
from .models import Debate

class DebateAdmin(admin.ModelAdmin):
    # Customize how debates are displayed in the admin list
    list_display = ('title', 'creator', 'status', 'scheduled_start_time')
    # Add filters for easy sorting
    list_filter = ('status', 'creator')
    # Add a search bar
    search_fields = ('title', 'description')

admin.site.register(Debate, DebateAdmin)