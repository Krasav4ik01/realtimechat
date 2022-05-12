import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path
from django.core.asgi import get_asgi_application

from chat.consumers import ChatConsumer
from public_chat.consumers import PublicChatConsumer
from notification.consumers import NotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtimechat.settings')


application = ProtocolTypeRouter({
    'http':  get_asgi_application(),
	
	'websocket': AuthMiddlewareStack(
			URLRouter([
					path('', NotificationConsumer.as_asgi()),
					path('chat/<room_id>/', ChatConsumer.as_asgi()),
					path('public_chat/<room_id>/', PublicChatConsumer.as_asgi()),
      				# re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
			])
		
	),
})


# application = ProtocolTypeRouter({
# 	'websocket': AllowedHostsOriginValidator(
# 		AuthMiddlewareStack(
# 			URLRouter([
# 					path('', NotificationConsumer),
# 					path('chat/<room_id>/', ChatConsumer),
# 					path('public_chat/<room_id>/', PublicChatConsumer),
# 			])
# 		)
# 	),
# })