from django.urls import path, include
from . import views
from rest_framework import routers
from .api import ProfileViewSet, ProfileHistoryViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'profile-history', ProfileHistoryViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profilepage', views.profilepage, name='profilepage'),
    path('activity', views.activity, name='activity'),
    path('settings', views.settings, name='settings'),

    path('api/', include(router.urls)),
]
