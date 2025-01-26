from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from accounts.models import Profile
from tasks.forms import CreateTaskForm
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


