from celery import shared_task
from datetime import timedelta
from accounts.models import Profile
from tasks_app.models import Tasks
from plyer import notification
import platform
from celery.schedules import crontab
from django.utils import timezone


@shared_task
def check_due_dates_task(request):
    from django.shortcuts import get_object_or_404

    user_profile = get_object_or_404(Profile, user=request.user)
    tasks = Tasks.objects.filter(profile=user_profile)

    for task in tasks:
        current_time = timezone.now()
        if task.due_date - current_time <= timedelta(minutes=30):
            if platform.system() == "Windows":
                notification.notify(
                    title="Attention!",
                    message=f"Task {task.name} almost passed the due date time",
                    app_name="Reminder_app",
                    timeout=5
                )
