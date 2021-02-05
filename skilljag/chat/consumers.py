import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils.timezone import now

@database_sync_to_async
def get_user_rooms(user):
    rooms =  user.rooms.all()
    room_ids = []
    for room in rooms:
        room_ids.append(str(room.id))
    return room_ids

class ChatConsumer(AsyncWebsocketConsumer):

    

    async def connect(self):
        print("zzzzzzzzzzzzzz")
        await self.accept()
        self.joined_rooms = await get_user_rooms(self.scope['user'])
        for room in self.joined_rooms:
            print("xxxxxxxxxxxxx")
            await self.channel_layer.group_add(
                'group_' + room,
                self.channel_name
            )

    async def disconnect(self, close_code):
        print("qqqqqqqqqqqqqqqqqq")
        # Leave room group
        for room in self.joined_rooms:
            print("aaaaaaaaaaaaaaa")
            await self.channel_layer.group_discard(
                'group_' + room,
                self.channel_name
            )

    # Receive message from WebSocket
    async def receive(self, text_data):
        print("****************")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        roomId = str(text_data_json['room_id'])
        room_group_name = 'group_' + roomId
        timestamp = str(now())
        createdBy = self.scope['user'].id
        # Send message to room group
        await self.channel_layer.group_send(
            room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'room_id': roomId,
                'timestamp': timestamp,
                'created_by': createdBy
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        print("################")
        message = event['message']
        roomId = event['room_id']
        timestamp = event['timestamp']
        createdBy = event['created_by']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'room_id': roomId,
            'timestamp': timestamp,
            'created_by': createdBy
        }))


""" import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from django.utils.timezone import now

def get_user_rooms(user):
    rooms =  user.rooms.all()
    room_ids = []
    for room in rooms:
        room_ids.append(str(room.id))
    return room_ids

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print("zzzzzzzzzzzzzz")
        self.accept()
        self.joined_rooms = get_user_rooms(self.scope['user'])
        for room in self.joined_rooms:
            print("xxxxxxxxxxxxx")
            async_to_sync(self.channel_layer.group_add)(
                'group_' + room,
                self.channel_name
            )

    def disconnect(self, close_code):
        print("qqqqqqqqqqqqqqqqqq")
        # Leave room group
        for room in self.joined_rooms:
            print("aaaaaaaaaaaaaaa")
            async_to_sync(self.channel_layer.group_discard)(
                'group_' + room,
                self.channel_name
            )

    # Receive message from WebSocket
    def receive(self, text_data):
        print("****************")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        roomId = str(text_data_json['room_id'])
        room_group_name = 'group_' + roomId
        timestamp = str(now())
        createdBy = self.scope['user'].id
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'room_id': roomId,
                'timestamp': timestamp,
                'created_by': createdBy
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        print("################")
        message = event['message']
        roomId = event['room_id']
        timestamp = event['timestamp']
        createdBy = event['created_by']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'room_id': roomId,
            'timestamp': timestamp,
            'created_by': createdBy
        })) """