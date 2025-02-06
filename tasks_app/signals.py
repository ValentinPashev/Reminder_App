from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Tasks
from .tasks import send_notification
import platform
from datetime import timedelta

@receiver(post_save, sender=Tasks)
def send_notification_reminder(sender, instance, created, **kwargs):
    if created:
        if instance.due_date:
            current_time = timezone.localtime(timezone.now())
            time_difference = instance.due_date - current_time

            soon_threshold = timedelta(hours=1)
            soon_threshold_seconds = soon_threshold.total_seconds()

            time_difference_seconds = time_difference.total_seconds()
            if 0 <= time_difference_seconds <= soon_threshold_seconds:
                title = f"Task Reminder: {instance.name}"
                message = "The task is due soon! Please check it!"

                print(f"Notification: {title} - {message}")

                if platform.system() == 'Windows':
                    send_notification(
                        title=title,
                        message=message,
                        time=time_difference_seconds
                    )
