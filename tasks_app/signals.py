from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import platform
from tasks_app.models import Tasks
from tasks_app.tasks import send_notification



@receiver(post_save, sender=Tasks)
def send_notification_reminder(sender, instance, created, **kwargs):
    if created:
        if sender.to_be_notified_on == timezone.now():
            title = f"Task Reminder: {instance.name}"
            message = "You have 30 minutes left to finish this task!"

            print(f"Notification: {title} - {message}")

            if platform.system() == 'Windows':
                send_notification.delay(
                    args=[title, message],
                    countdown=10
                )

