from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView
from accounts.models import Profile
from tasks.forms import CreateTaskForm, SearchForm
from tasks.models import Tasks

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

