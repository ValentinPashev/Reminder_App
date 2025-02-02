from django import forms

from tasks_app.models import Tasks


class BaseTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'due_date',)

        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
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
