
from celery import shared_task
from plyer import notification
import platform
from django.utils import timezone

@shared_task
def send_notification(title, message, time):
    if abs(time - timezone.localtime(timezone.now())).total_seconds() < 60:
        if platform.system() == 'Windows':
            notification.notify(
                title=title,
                message=message,
                timeout=10
            )

    else:
        print(f"Notification {title} will be triggered later.")



