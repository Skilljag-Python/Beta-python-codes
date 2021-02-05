from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MessageViewSet, RoomViewSet

router = DefaultRouter()
router.register(r"rooms", RoomViewSet,basename='rooms')
router.register(r"messages", MessageViewSet,basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]