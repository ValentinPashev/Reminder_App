from django.db import models
from datetime import datetime, timedelta
from accounts.models import Profile
from tasks.choices import StatusChoices


class Tasks(models.Model):
    name = models.CharField(
        max_length=100
    )

    description = models.TextField(

    )

    date_created = models.DateTimeField(
        auto_now_add=True
    )

    due_date = models.DateTimeField(

    )

    now = datetime.now()
    time_after_30_min = now + timedelta(minutes=30)

    due_time = models.TimeField(
        default=time_after_30_min
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="user_tasks",
        null=True,
        blank=True
    )

    status = models.CharField(
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
        max_length=100,
    )

    completed = models.BooleanField(
        default=False
    )
    def __str__(self):
        return self.name