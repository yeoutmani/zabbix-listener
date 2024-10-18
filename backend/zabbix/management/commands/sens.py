from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from zabbix.tasks import fetch_and_broadcast_zabbix_problems

class Command(BaseCommand):
    help = "Send a test message to the zabbix_problems group"

    def handle(self, *args, **kwargs):
        fetch_and_broadcast_zabbix_problems()
        self.stdout.write(self.style.SUCCESS("message sent!"))
