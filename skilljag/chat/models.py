from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    created_by = models.ForeignKey(User, related_name='messages',on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats',blank =True)
    messages = models.ManyToManyField(Message, blank=True)

