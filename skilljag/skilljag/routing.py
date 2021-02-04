from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

class APIDemultiplexer(WebsocketDemultiplexer):

    mapping = {
      'chats': 'chats_channel'
    }

channel_routing = [
    route_class(APIDemultiplexer)
]