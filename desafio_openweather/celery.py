import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desafio_openweather.settings")

app = Celery("desafio_openweather")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
