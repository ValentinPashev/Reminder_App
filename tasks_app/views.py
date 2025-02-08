from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView, UpdateView, DeleteView
from accounts.models import Profile
from tasks_app.forms import CreateTaskForm, SearchForm, EditTaskForm, AddingHoursForm, DeleteTaskForm
from tasks_app.models import Tasks


UserModel = get_user_model()


class CreateTaskView(CreateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = 'tasks/create-task.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.profile = profile
        return super().form_valid(form)


class DashboardView(ListView, FormView):
    template_name = 'tasks/dashboard.html'
    context_object_name = 'tasks'
    form_class = SearchForm
    paginate_by = 8
    model = Tasks
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        user_profile = self.request.user.profile
        queryset = self.model.objects.filter(profile=user_profile).exclude(status='Done')

        return queryset


class DoneDashboardView(ListView):
    model = Tasks
    template_name = 'tasks/task-done-dashboard.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user_profile = self.request.user.profile
        queryset = self.model.objects.filter(profile=user_profile).filter(status='Done')

        return queryset


def done(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.status = 'Done'
    task.save()

    next_url = request.GET.get('next', 'dashboard')
    return redirect(next_url)

class TaskDetailsView(DetailView):
    model = Tasks
    template_name = 'tasks/task-details.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def add_time(request, pk):
    task = Tasks.objects.get(pk=pk)
    form = AddingHoursForm()
    if request.method == "POST":
        form = AddingHoursForm(request.POST)
        if form.is_valid():
            task.due_date += timedelta(hours=form.cleaned_data['number'])
            task.save()
            context = {
                'task': task,
                'form': form,
            }
            return redirect('dashboard')

    return render(request, 'tasks/add_time.html', {'form': form, 'task': task})

def overdue(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    user_tasks = Tasks.objects.filter(profile=user_profile)

    for task in user_tasks:
        if task.status == 'Pending' and timezone.localtime(timezone.now()) > task.due_date:
            task.status = 'Overdue'
            task.save()
        elif task.status == 'Overdue' and timezone.localtime(timezone.now()) < task.due_date:
            task.status = 'Pending'
            task.save()

    next_url = request.GET.get('next', 'dashboard')
    return redirect(next_url)

class EditTaskView(UpdateView):
    model = Tasks
    form_class = EditTaskForm
    template_name = 'tasks/edit-tasks.html'
    success_url = reverse_lazy('dashboard')

class DeleteTaskView(DeleteView, FormView):
    model = Tasks
    form_class = DeleteTaskForm
    template_name = 'tasks/delete-task.html'
    success_url = reverse_lazy("dashboard")

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        task = Tasks.objects.get(pk=pk)
        return task.__dict__