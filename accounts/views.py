from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import RedirectURLMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from accounts.forms import CustomCreationForm


# Create your views here.
class UserRegistrationView(CreateView):
    form_class = CustomCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')