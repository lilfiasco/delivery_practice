# Python
from os import environ

# Third party
from celery import Celery
from celery.schedules import crontab

# Django
from django.conf import settings


environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'settings.settings'
)
app: Celery = Celery(
    'settings',
    broker=settings.CELERY_BROKER_URL,
    include=(
        'apps.auths.tasks',
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
        'task': 'check_order_status',
        'schedule': crontab(minute='*/1')
    }
}

app.conf.broker_connection_retry_on_startup = True

app.conf.timezone = 'Asia/Almaty'