from django import forms

from tasks.models import Tasks


class BaseTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'


class CreateTaskForm(BaseTaskForm):
    pass