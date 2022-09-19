from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path, include, re_path
from django.conf.urls import url

from personal.consumer import ChatConsumer

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
    URLRouter([
      re_path(r'chatroompage/(?P<room_name>\w+)/$', ChatConsumer),
    ])
  )
})