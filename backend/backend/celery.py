import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "backend.settings"
)  # Replace 'myproject' with your project name

# Create a new Celery application instance
app = Celery("backend")  # Replace 'myproject' with your project name

# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
