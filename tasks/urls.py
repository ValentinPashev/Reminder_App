from django.urls import path, include
from tasks.views import CreateTaskView, DashboardView, TaskDetailsView

urlpatterns = [
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('task_dashboard/', DashboardView.as_view(), name='dashboard'),
    path('<int:pk>/', include([
        path('task-details/', TaskDetailsView.as_view(), name='task_details'),
    ])),
]