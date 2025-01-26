from django.contrib import admin
from django.urls import path, include
import tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('', include('common.urls')),
    path('accounts/', include('accounts.urls')),
]