from rest_framework import serializers
from .models import Profile, ProfileHistory

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileHistory
        fields = '__all__'