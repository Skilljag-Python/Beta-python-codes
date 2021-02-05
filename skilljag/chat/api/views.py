from .serializers import MessageSerializer, RoomSerializer
from django.utils.timezone import now
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.db import models
from ..models import Room,Message

class RoomViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = self.request.user.rooms.all()
        return queryset


class MessageViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)


