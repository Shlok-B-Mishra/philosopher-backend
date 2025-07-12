# config/urls.py

from django.contrib import admin
from django.urls import path, include # Make sure to import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add these lines for our API endpoints
    path('api/v1/debates/', include('debates.urls')),
    path('api/v1/users/', include('users.urls')),
]