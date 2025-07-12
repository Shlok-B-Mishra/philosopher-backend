# debates/urls.py

from django.urls import path
from .views import DebateList, DebateDetail

urlpatterns = [
    path('', DebateList.as_view(), name='debate-list'),
    path('<int:pk>/', DebateDetail.as_view(), name='debate-detail'),
]