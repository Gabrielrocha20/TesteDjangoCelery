import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings")
app = Celery("Project", result_extended=True)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
