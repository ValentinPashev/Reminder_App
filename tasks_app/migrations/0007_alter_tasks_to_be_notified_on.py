# Generated by Django 5.1.5 on 2025-02-02 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0006_alter_tasks_to_be_notified_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='to_be_notified_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 2, 20, 54, 43, 440249, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
