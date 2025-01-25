from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Tasks(models.Model):
    name = models.CharField(
        max_length=100
    )

    description = models.TextField(

    )

    done = models.BooleanField(
        default=False
    )

    date_created = models.DateTimeField(
        auto_now_add=True
    )

    due_date = models.DateTimeField(

    )

    def __str__(self):
        return self.name