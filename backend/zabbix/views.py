from django.shortcuts import render
from .tasks import fetch_and_broadcast_zabbix_problems

def zabbix_problems_view(request):
    return render(request, "zabbix/zabbix_problems.html")
