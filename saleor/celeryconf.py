import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

app = Celery('saleor')

CELERY_TIMEZONE = 'Europe/Moscow'

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
