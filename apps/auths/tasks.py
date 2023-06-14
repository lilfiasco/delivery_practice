# Python
from typing import Any
from datetime import timedelta

# Django
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


# First party
from settings.celery import app

# Local
from .models import Order


@app.task(
    name='check-order-status'
)
def check_order_status(*args: Any) -> None:
    
    current_time = timezone.now()
    time_limit = current_time - timedelta(minutes=30)

    Order.objects.filter(is_done=False, datetime_created__gte=time_limit).delete()
