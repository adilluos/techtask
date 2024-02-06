from .models import Profile, ProfileHistory
from rest_framework import viewsets, permissions
from .serializers import ProfileSerializer, ProfileHistorySerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileSerializer

class ProfileHistoryViewSet(viewsets.ModelViewSet):
    queryset = ProfileHistory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileHistorySerializer