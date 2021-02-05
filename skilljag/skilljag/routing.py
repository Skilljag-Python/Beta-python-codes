""" from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

class APIDemultiplexer(WebsocketDemultiplexer):

    mapping = {
      'chats': 'chats_channel'
    }

channel_routing = [
    route_class(APIDemultiplexer)
] """

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import django_chatter

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            django_chatter.routing.websocket_urlpatterns
        )
    ),
})