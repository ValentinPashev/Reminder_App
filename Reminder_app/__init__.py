from __future__ import absolute_import, unicode_literals
import tasks_app
from .celery import app as celery_app

__all__ = ('tasks',)
