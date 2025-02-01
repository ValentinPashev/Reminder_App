from datetime import time, timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import title
from django.utils import timezone
import platform
from win10toast import ToastNotifier
from plyer import notification
from .models import Tasks





@receiver(post_save, sender=Tasks)
def task_overdue(sender, instance,  **kwargs):
    calculated_time = instance.calculate_remaining_time()

    if instance.status != 'Done':
        if timedelta(minutes=30) >= calculated_time > timedelta(0):
            title = f"Task Reminder: {instance.name}"
            message = "You have 30 minutes left to finish this task!"

            print(f"Notification: {title} - {message}")

            if platform.system() == 'Windows':
                notification.notify(title=title, message='You have 30 minutes left to finish this task!', app_name='tasks',
                                    app_icon='',
                                    timeout=10, )