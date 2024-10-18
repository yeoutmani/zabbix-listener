from django.urls import path
from .views import zabbix_problems_view

urlpatterns = [
    path("problems/", zabbix_problems_view, name="zabbix_problems"),
]
