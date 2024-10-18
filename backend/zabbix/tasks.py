from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from zabbix_utils import ZabbixAPI
from celery import shared_task
import json

def fetch_and_broadcast_zabbix_problems():
    ZABBIX_SERVER = "http://localhost:8882/api_jsonrpc.php"
    ZABBIX_USER = "Admin"
    ZABBIX_PASSWORD = "zabbix"

    try:
        zabbix = ZabbixAPI(url=ZABBIX_SERVER)
        zabbix.login(user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        problems = zabbix.problem.get()

        if not problems:
            print("No problems found.")
        else:
            print(f"Fetched {len(problems)} problems from Zabbix.")

        problems_json = json.dumps(problems)
        print(problems_json)
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            "zabbix_problems",  # Group name
            {
                "type": "zabbix_problem_message",
                "message": problems_json,
            },
        )

        print("Broadcasted problems to WebSocket group.")

    except Exception as e:
        print(f"Error occurred: {e}")


@shared_task
def broadcast_zabbix_problems():
    print('hii')
    fetch_and_broadcast_zabbix_problems()
