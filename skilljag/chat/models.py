from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):

    participants = models.ManyToManyField(User, related_name="rooms", blank =True)
    pending_participants = models.ManyToManyField(User, related_name="pending_rooms", blank =True)


class Message(models.Model):

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')