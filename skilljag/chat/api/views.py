from .serializers import MessageSerializer, RoomSerializer
from django.utils.timezone import now
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.db import models
from ..models import Room,Message
from django.contrib.auth.models import User


class RoomViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):

        query_dict = {}

        for k in self.request.query_params.keys():
            query_dict[k] = self.request.query_params.getlist(k)

        if 'pending' in query_dict.keys():

            para = query_dict.get('pending')[0]
            queryset = self.request.user.pending_rooms.all()

        elif 'uid' in query_dict.keys():

            uid = query_dict.get('uid')[0]
            user1 = self.request.user
            user2 = User.objects.get(id=uid)
            filters = models.Q()
            filters &=(models.Q(participants__id = user1.id) | models.Q(pending_participants__id = user1.id))
            filters &=(models.Q(participants__id = user2.id) | models.Q(pending_participants__id = user2.id))
            
            queryset = Room.objects.filter(filters)
            if len(queryset) == 0:
                room = Room.objects.create()
                room.participants.add(user1)
                room.pending_participants.add(user2)
                room.save()
                

            queryset = Room.objects.filter(filters)
        
        else:

            queryset = self.request.user.rooms.all()
        
        return queryset

    def paginate_queryset(self, queryset):
        return None


class MessageViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated,]



    def perform_create(self, serializer):
        message = serializer.save(created_by = self.request.user)
        """ room_id = message.room_id(serializer)
        room = Room.objects.get(id = room_id) """

        room = message.room
            
        if(self.request.user in room.pending_participants.all()):
            room.participants.add(self.request.user)
            room.pending_participants.remove(self.request.user)


