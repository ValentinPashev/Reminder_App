from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks_app/', include('tasks_app.urls')),
    path('', include('common.urls')),
    path('accounts/', include('accounts.urls')),
]