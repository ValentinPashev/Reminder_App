from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomCreationForm, ProfileInformationForm


# Create your views here.
class UserRegistrationView(CreateView):
    form_class = CustomCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')


def profile_information_view(request):
    profile = request.user.profile

    is_profile_complete = all([
        profile.first_name,
        profile.last_name,
        profile.age,
        profile.occupation,
    ])

    if is_profile_complete:
        activity_logs = profile.activity_logs.all()
        context = {
            'profile': profile,
            'activity_logs': activity_logs,
        }

        return context
    #TODO: html template for this!!!

    else:
        if request.method == 'POST':
            form = ProfileInformationForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('dashboard'))
        else:
            form = ProfileInformationForm(instance=profile)
            print(form.errors)

        context = {
            'form': form,
        }

        return render(request, 'accounts/profile_creation.html', context)