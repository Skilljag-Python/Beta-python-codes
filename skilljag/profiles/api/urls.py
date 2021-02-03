from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import ProfileFollowerViewSet, ProfileViewSet, AvatarImageViewSet

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet,basename='profiles')
router.register(r"avatars", AvatarImageViewSet,basename='avatars')
router.register(r"followers", ProfileFollowerViewSet,basename='followers')

urlpatterns = [
    path('', include(router.urls)),
]