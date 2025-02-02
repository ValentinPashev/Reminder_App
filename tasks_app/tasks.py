from celery import shared_task
import platform
from plyer import notification



@shared_task
def send_notification(title, message):
    print(f"Notification: {title} - {message}")

    if platform.system() == 'Windows':
        notification.notify(
            title=title,
            message=message,
            app_name='tasks_app',
            timeout=10
        )
