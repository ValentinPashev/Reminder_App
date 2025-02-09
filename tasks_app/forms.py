from django.utils import timezone
from django import forms
from tasks_app.mixins import DisableFieldsMixin
from tasks_app.models import Tasks


class BaseTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        exclude = ('to_be_notified_on', 'profile', 'status',)

class CreateTaskForm(BaseTaskForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'due_date')
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

class EditTaskForm(CreateTaskForm):
    pass


class AddingHoursForm(forms.Form):
    number = forms.IntegerField()

class DeleteTaskForm(BaseTaskForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)

class SetNewDueDateForm(forms.Form):
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        help_text="Due date with time and hour"
    )

    def clean_due_date(self):
        due_date = self.cleaned_data.get("due_date")
        if due_date < timezone.now():
            raise forms.ValidationError("The date needs to be in the future!")
        return due_date