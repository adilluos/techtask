import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to='profile_images', default='blank_profile_image.jpg')
    name = models.CharField(null=True, max_length=50)
    surname = models.CharField(null=True, max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(null=True, max_length=15)
    age = models.IntegerField(null=True)
    profession = models.CharField(null=True, max_length=50)
    about_me = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class ProfileHistory(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20)  # 'creation', 'update', 'login', 'logout'
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username}'s History Entry"