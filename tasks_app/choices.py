from django.db import models


class StatusChoices(models.TextChoices):
    DONE = "Done", "Done"
    PENDING = "Pending", "Pending"
    OVERDUE = "Overdue", "Overdue"