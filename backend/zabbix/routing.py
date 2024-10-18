from django.urls import re_path
from .consumers import ZabbixProblemsConsumer

websocket_urlpatterns = [
    re_path(r"ws/zabbix/problems/$", ZabbixProblemsConsumer.as_asgi()),
]
