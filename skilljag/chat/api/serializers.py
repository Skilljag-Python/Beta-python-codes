from ..models import Message, Room
from rest_framework import serializers
from profiles.api.serializers import UserCompactSerializer
from django.contrib.auth.models import User

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['created_by']


class RoomSerializer(serializers.ModelSerializer):

    participants = UserCompactSerializer(many = True, read_only = True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id','participants','messages']
