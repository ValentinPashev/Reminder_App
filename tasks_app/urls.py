from django.urls import path, include

from tasks_app import views
from tasks_app.views import CreateTaskView, DashboardView, TaskDetailsView, DoneDashboardView, EditTaskView, \
    DeleteTaskView

urlpatterns = [
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('task_dashboard/', DashboardView.as_view(), name='dashboard'),
    path('done_tasks/', DoneDashboardView.as_view(), name='done_dashboard'),
    path('refresh_tasks/', views.overdue, name="overdue"),
    path('<int:pk>/', include([
        path('task-details/', TaskDetailsView.as_view(), name='task_details'),
        path('done/', views.done, name='task_done'),
        path('add_time/', views.add_time, name='add_time'),
        path('choose_time_option/', views.choose_time_set_option, name='choose_time_set_option'),
        path('set_new_duedate/', views.set_new_due_date, name='set_new_due_date'),
        path('edit_task/', EditTaskView.as_view(), name='edit_task'),
        path('delete/', DeleteTaskView.as_view(), name='delete'),
    ])),
]