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

print("CHECK CELERY AAAA")

@app.task(
    name='check-order-status',
    bind=True
)
def check_order_status(*args: Any) -> None:
    
    print("CHECK CELERY 2 AAAA")
    # current_time = timezone.now()
    # time_limit = current_time - timedelta(minutes=30)

    # Order.objects.filter(is_done=False, datetime_created__gte=time_limit).delete()
