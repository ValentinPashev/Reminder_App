from django.utils import timezone
from django.db import models
from datetime import timedelta
from django.utils.timezone import now
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
        help_text="Краен срок с дата и час"
    )
    remaining = models.DurationField(
        null=True,
        blank=True,
        help_text="Оставащо време до крайния срок"
    )

    def calculate_remaining_time(self):
        if self.due_date:
            if self.due_date.tzinfo is None:
                self.due_date = timezone.make_aware(self.due_date, timezone.get_current_timezone())
            current_time = timezone.now()

            remaining_time = self.due_date - current_time
            if remaining_time.total_seconds() > 0:
                return remaining_time
            else:
                return timedelta(0)
        return timedelta(0)

    def formatted_remaining_time(self):
        remaining_time = self.calculate_remaining_time()
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours}:{minutes:02d}"

    def is_overdue(self, save=True):
        if now() > self.due_date:
            self.status = StatusChoices['Overdue']
        else:
            self.status = StatusChoices['Done']
        if save:
            self.save()

        return self.status

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



    def __str__(self):
        return self.name