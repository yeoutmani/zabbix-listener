import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from zabbix.consumers import ZabbixProblemsConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    # URL routing for the WebSocket
                    path("ws/zabbix/problems/", ZabbixProblemsConsumer.as_asgi()),
                ]
            )
        ),
    }
)
