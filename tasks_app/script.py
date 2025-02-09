from datetime import timedelta
import platform

from django.shortcuts import get_object_or_404
from plyer import notification
from django.utils import timezone

from accounts.models import Profile
from tasks_app.models import Tasks


def check_due_dates(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    tasks = Tasks.objects.filter(profile=user_profile)

    for task in tasks:
        current_time = timezone.now()
        if task.due_date - current_time <= timedelta(minutes=30):
            if platform.system() == "Windows":
                notification.notify(
                    title=f"Attention!",
                    message=f"Task {task.name} almost passed the due date time",
                    app_name="Reminder_app",
                    timeout=5
                )