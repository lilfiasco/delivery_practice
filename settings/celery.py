# Python
from os import environ

# Third party
from celery import Celery
from celery.schedules import crontab

# Django
from django.conf import settings


environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'settings.base'
)
app: Celery = Celery(
    'settings',
    broker=settings.CELERY_BROKER_URL,
    include=(
        'main.tasks',
    )
)
app.config_from_object(
    'django.conf:settings', namespace='CELERY'
)
app.autodiscover_tasks(
    lambda: settings.PROJECT_APPS
)
app.conf.beat_schedule = {
    'every-1-minute-every-day': {
        'task': 'check-order-status',
        'schedule': crontab(minute='*/10')
    }
}
app.conf.timezone = 'UTC'