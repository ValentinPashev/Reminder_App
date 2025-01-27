from django import forms
from django.forms import SelectDateWidget

from tasks.models import Tasks


class BaseTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'due_date', 'due_time')

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=35,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a task',
            }
        )
    )
